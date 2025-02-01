from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What are Django’s Migrations?",
            answer="Migrations in Django are a way of propagating changes made to the models (database schema) into the database schema itself. It is a mechanism to manage and apply schema changes to the database. It allows developers to keep track of database changes over time in a structured and version-controlled way.",
        )

    def test_translation(self):
        translated = self.faq.get_translated_question('hi')
        self.assertIsNotNone(translated)

    def test_api_response(self):
        response = self.client.get(f'/api/faqs/{self.faq.id}/?lang=hi')
        self.assertEqual(response.status_code, 200)
