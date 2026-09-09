from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
class HomeViewTest(TestCase):

    # test de l'url de la page d'accueil
    def test_home_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # test du contenu de la page d'accueil
    def test_home_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Hello Django!')