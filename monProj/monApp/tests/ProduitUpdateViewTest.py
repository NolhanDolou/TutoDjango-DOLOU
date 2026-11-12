from datetime import date

from django.test import TestCase
from django.urls import reverse

from monApp.models import Produit


class ProduitUpdateViewTest(TestCase):
    def test_produit_update_view_post_valid(self):
        produit = Produit.objects.create(
            intituleProd="ProduitAvantModification",
            prixUnitaireProd=100.0,
            dateFabProd=date(2023, 1, 1),
        )
        data = {
            "intituleProd": "ProduitApresModification",
            "prixUnitaireProd": 150.0,
            "dateFabProd": "01/02/2024",
        }

        response = self.client.post(
            reverse("modificationProduit", args=[produit.pk]), data
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Produit.objects.count(), 1)
        produit.refresh_from_db()
        self.assertEqual(produit.intituleProd, "ProduitApresModification")
        self.assertEqual(produit.prixUnitaireProd, 150.0)
        self.assertEqual(produit.dateFabProd, date(2024, 2, 1))
