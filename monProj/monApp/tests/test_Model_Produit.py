from django.test import TestCase
from monApp.models import Produit

class ProduitModelTest(TestCase):
    def setUp(self):
        # créer attribut produit a utiliser dans les tests
        self.prod = Produit.objects.create(intituleProd="ProdTest",
                                            prixUnitaireProd=10.0
                                           )

    def test_prod_creation(self):
        self.assertEqual(self.prod.intituleProd, "ProdTest")

    def test_string_representation(self):
        self.assertEqual(str(self.prod), "ProdTest")

    def test_prod_updating(self):
        self.prod.intituleProd = "ProdTestModifie"
        self.prod.save()
        # Récup obj maj
        updated_prod = Produit.objects.get(refProd=self.prod.refProd)
        self.assertEqual(updated_prod.intituleProd, "ProdTestModifie")

    def test_prod_deletion(self):
        self.prod.delete()
        self.assertEqual(Produit.objects.count(),0)