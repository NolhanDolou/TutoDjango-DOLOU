from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from monApp.models import Produit


class ProduitViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testeur", "testeur@example.com", "MotDePasse123"
        )
        self.client.force_login(self.user)


class ProduitCreateViewTest(ProduitViewTestCase):
    def test_anonymous_user_is_redirected_to_login(self):
        self.client.logout()

        response = self.client.get(reverse("creationProduit"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('creationProduit')}",
        )

    def test_categorie_create_view_post_valid(self):
        data = {
            "intituleProd": "ProduitPourTestCreation",
            "prixUnitaireProd": 100.0,
            "dateFabProd": date(2023, 1, 1),
            "categorie": "",
            "statut": "",
        }
        # simulation soumission formulaire
        response = self.client.post(reverse('creationProduit'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Produit.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Produit.objects.last().intituleProd, 'ProduitPourTestCreation')


class ProduitUpdateViewTest(ProduitViewTestCase):
    def test_produit_update_view_get(self):
        produit = Produit.objects.create(
            intituleProd="ProduitAvantModification",
            prixUnitaireProd=100.0,
        )
        response = self.client.get(reverse('modificationProduit', args=[produit.pk]))
        self.assertEqual(response.status_code, 200)

    def test_produit_update_view_post_valid(self):
        produit = Produit.objects.create(
            intituleProd="ProduitAvantModification",
            prixUnitaireProd=100.0,
        )
        data = {
            "intituleProd": "ProduitApresModification",
            "prixUnitaireProd": 150.0,
            "dateFabProd": date(2023, 1, 1),
            "categorie": "",
            "statut": "",
        }
        response = self.client.post(reverse('modificationProduit', args=[produit.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Produit.objects.count(), 1)
        produit.refresh_from_db()
        self.assertEqual(produit.intituleProd, 'ProduitApresModification')


class ProduitDeleteViewTest(ProduitViewTestCase):
    def test_produit_delete_view_get(self):
        produit = Produit.objects.create(
            intituleProd="ProduitPourSuppression",
            prixUnitaireProd=100.0,
        )
        response = self.client.get(reverse('suppressionProduit', args=[produit.pk]))
        self.assertEqual(response.status_code, 200)

    def test_produit_delete_view_post_valid(self):
        produit = Produit.objects.create(
            intituleProd="ProduitPourSuppression",
            prixUnitaireProd=100.0,
        )
        response = self.client.post(reverse('suppressionProduit', args=[produit.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Produit.objects.count(), 0)