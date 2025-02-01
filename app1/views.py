from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    @action(detail=True, methods=['get'])
    def translate(self, request, pk=None):
        faq = self.get_object()
        lang = request.query_params.get('lang', 'en')
        translated_text = faq.get_translated_question(lang)
        return Response({'question': translated_text, 'answer': faq.answer})
