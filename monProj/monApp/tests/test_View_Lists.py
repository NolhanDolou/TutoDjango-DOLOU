from django.test import TestCase
from django.urls import reverse

class ListViewTest(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(nomCat="Boissons")
        self.rayon = Rayon.objects.create(nomRayon="Rayon A")
        self.statut = Statut.objects.create(libelleStatut="Disponible")
        self.produit = Produit.objects.create(intituleProd="Coca-Cola")


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
