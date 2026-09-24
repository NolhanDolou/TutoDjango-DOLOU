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
        response = self.client.get(reverse('home', args=["test"]))
        self.assertContains(response, 'Hello test!')

    def test_contact_content(self):
        response = self.client.get(reverse('contact'))
        self.assertContains(response, '<h1>Bienvenue sur la page de contact</h1>')

    def test_aboutus_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, "<h1>Bienvenue sur la page d'infomations</h1>")


#----------------------------------------------------------------------------------
class ListViewTest(TestCase):

    # test de l'url de la page d'accueil
    def test_lst_prod_status_code(self):
        response = self.client.get(reverse('ListeProduits'))
        self.assertEqual(response.status_code, 200)

    def test_lst_cate_status_code(self):
        response = self.client.get(reverse('ListeCategories'))
        self.assertEqual(response.status_code, 200)

    def test_lst_rn_status_code(self):
        response = self.client.get(reverse('ListeRayons'))
        self.assertEqual(response.status_code, 200)

    def test_lst_stt_status_code(self):
        response = self.client.get(reverse('ListeStatuts'))
        self.assertEqual(response.status_code, 200)


#----------------------------------------------------------------------------------
    # test du contenu de la page d'accueil
    # def test_lst_prod_content(self):
    #     response = self.client.get(reverse('ListeProduits'))
    #     self.assertContains(response, '')