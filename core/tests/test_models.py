from django.test import TestCase
from model_mommy import mommy


class ServiceTestCase(TestCase):
    def setUp(self):
        self.pergunta = mommy.make("Question")

    def test_str(self):
        self.assertEquals(str(self.pergunta), self.pergunta.pergunta)
