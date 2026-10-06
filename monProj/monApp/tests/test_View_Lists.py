from django.test import TestCase
from django.urls import reverse
from monApp.models import Produit, Categorie, Rayon, Statut

class ListViewTest(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(nomCat="Boissons")
        self.rayon = Rayon.objects.create(nomRayon="Rayon A")
        self.statut = Statut.objects.create(libelleStatut="Disponible")
        self.produit = Produit.objects.create(
            intituleProd="Coca-Cola",
            prixUnitaireProd=1.50,
            categorie=self.categorie,
            statut=self.statut,
        )


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

    def test_liste_produits_content(self):
        response = self.client.get(reverse('ListeProduits'))
        self.assertContains(response, f"<li>{self.produit.intituleProd}</li>")

    def test_liste_categories_content(self):
        response = self.client.get(reverse('ListeCategories'))
        self.assertContains(response, f"<li>{self.categorie.nomCat}</li>")

    def test_liste_rayons_content(self):
        response = self.client.get(reverse('ListeRayons'))
        self.assertContains(response, f"<li>{self.rayon.nomRayon}</li>")

    def test_liste_statuts_content(self):
        response = self.client.get(reverse('ListeStatuts'))
        self.assertContains(response, f"<li>{self.statut.libelleStatut}</li>")