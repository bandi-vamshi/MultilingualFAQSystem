from django.db import models
from django.utils.translation import gettext_lazy as _
from googletrans import Translator
from django.core.cache import cache
from ckeditor.fields import RichTextField
import redis

# Setting up Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

class FAQ(models.Model):
    question = models.TextField(verbose_name=_("Question"))
    answer = RichTextField(verbose_name=_("Answer"))
    language_code = models.CharField(max_length=10, default='en', verbose_name=_("Language"))
    question_hi = models.TextField(null=True, blank=True, verbose_name=_("Question in Hindi"))
    question_bn = models.TextField(null=True, blank=True, verbose_name=_("Question in Bengali"))

    def translate_question(self, lang_code):
        cache_key = f"faq_{self.id}_{lang_code}"
        cached_translation = redis_client.get(cache_key)
        
        if cached_translation:
            return cached_translation.decode('utf-8')

        translator = Translator()
        translated_text = translator.translate(self.question, src='en', dest=lang_code).text
        
        redis_client.set(cache_key, translated_text, ex=86400)
        return translated_text

    def get_translated_question(self, lang_code):
        if lang_code == 'hi':
            return self.question_hi or self.translate_question('hi')
        elif lang_code == 'bn':
            return self.question_bn or self.translate_question('bn')
        return self.question

    def save(self, *args, **kwargs):
        translator = Translator()
        self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question[:50]
