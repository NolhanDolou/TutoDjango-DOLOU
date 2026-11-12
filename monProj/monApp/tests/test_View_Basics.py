from datetime import date

from django.core import mail
from django.test import TestCase
from django.urls import reverse

from monApp.models import Categorie, Produit, Rayon, Statut


class HomeViewTest(TestCase):

    # test de l'url de la page d'accueil
    def test_home_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_param_status_code(self):
        response = self.client.get(reverse('home', args=["test"]))
        self.assertEqual(response.status_code, 200)

    def test_contact_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_email_sent_status_code(self):
        response = self.client.get(reverse('email-sent'))
        self.assertEqual(response.status_code, 200)
#----------------------------------------------------------------------------------
    # test du contenu de la page d'accueil
    def test_home_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Welcome, this is the home page')

    def test_home_param_content(self):
        response = self.client.get(reverse('home', args=["test"]))
        self.assertContains(response, 'Hello test!')

    def test_contact_content(self):
        response = self.client.get(reverse('contact'))
        self.assertContains(response, 'Contact Us')

    def test_aboutus_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, "Welcome, this is the about page")

    def test_email_sent_content(self):
        response = self.client.get(reverse('email-sent'))
        self.assertContains(response, "Votre message a bien été envoyé.")
#----------------------------------------------------------------------------------
    # test de la soumission du formulaire de contact (ContactView.form_valid)
    def test_contact_post_valid(self):
        data = {
            "name": "Testeur",
            "email": "testeur@example.com",
            "message": "Bonjour, ceci est un message de test.",
        }
        # simulation soumission formulaire
        response = self.client.post(reverse('contact'), data)
        # Vérifie la redirection après l'envoi
        self.assertRedirects(response, reverse('email-sent'))
        # Vérifie qu'un mail a été envoyé
        self.assertEqual(len(mail.outbox), 1)
        # Vérifie le contenu du mail envoyé
        self.assertEqual(mail.outbox[0].subject, 'Message from Testeur via MonProjet Contact Us form')
        self.assertEqual(mail.outbox[0].body, "Bonjour, ceci est un message de test.")
        self.assertEqual(mail.outbox[0].to, ["admin@monprojet.com"])


#----------------------------------------------------------------------------------
class ListViewTest(TestCase):

    # test de l'url des pages de liste
    def test_lst_prod_status_code(self):
        response = self.client.get(reverse('listProduits'))
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
class DetailViewTest(TestCase):

    # test de l'url et du contexte des pages de détail
    def test_detail_produit(self):
        produit = Produit.objects.create(
            intituleProd="ProduitPourTestDetail",
            prixUnitaireProd=10.0,
            dateFabProd=date(2023, 1, 1),
            categorie=None,
            statut=None,
        )
        response = self.client.get(reverse('detailProduit', args=[produit.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], "Détail du produit")

    def test_detail_categorie(self):
        categorie = Categorie.objects.create()
        response = self.client.get(reverse('detailCategorie', args=[categorie.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], "Détail de la catégorie")

    def test_detail_rayon(self):
        rayon = Rayon.objects.create()
        response = self.client.get(reverse('detailRayon', args=[rayon.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], "Détail du rayon")

    def test_detail_statut(self):
        statut = Statut.objects.create()
        response = self.client.get(reverse('detailStatut', args=[statut.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], "Détail du statut")


#----------------------------------------------------------------------------------
class CreateViewGetTest(TestCase):

    # test de l'affichage (GET) des pages de création
    def test_create_produit_get(self):
        response = self.client.get(reverse('creationProduit'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], "Ajout d'un nouveau produit")

    def test_create_categorie_get(self):
        response = self.client.get(reverse('creationCategorie'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], "Ajout d'une nouvelle catégorie")

    def test_create_rayon_get(self):
        response = self.client.get(reverse('creationRayon'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], "Ajout d'un nouveau rayon")

    def test_create_statut_get(self):
        response = self.client.get(reverse('creationStatut'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['titremenu'], "Ajout d'un nouveau statut")