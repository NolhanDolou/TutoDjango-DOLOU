from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):

    # test de l'url de la page d'accueil
    def test_home_status_code(self):
                    response = self.client.get(reverse('default'))
                    self.assertEqual(response.status_code, 200)
    
    def test_home_param_status_code(self):
        response = self.client.get(reverse('home', args=["test"]))
        self.assertEqual(response.status_code, 200)

    def test_contact_status_code(self):
            response = self.client.get(reverse('contact'))
            self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
            response = self.client.get(reverse('aboutus'))
            self.assertEqual(response.status_code, 200)
#----------------------------------------------------------------------------------
    # test du contenu de la page d'accueil
    def test_home_content(self):
        response = self.client.get(reverse('default'))
        self.assertContains(response, 'Hello default!')

    def test_home_param_content(self):
            response = self.client.get(reverse('home', args="test"))
            self.assertContains(response, 'Hello test!')

    def test_contact_content(self):
            response = self.client.get(reverse('contact'))
            self.assertContains(response, 'Bienvenue sur la page de contact!')

    def test_home_content(self):
            response = self.client.get(reverse('aboutus'))
            self.assertContains(response, "Bienvenue sur la page d'infomations")