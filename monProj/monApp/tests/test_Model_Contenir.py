from django.test import TestCase
from monApp.models import Contenir, Produit, Rayon

class ContenirModelTest(TestCase):
    def setUp(self):
        # créer attribut contenir a utiliser dans les tests
        self.prod = Produit.objects.create(intituleProd="ProdTest",
                                                    prixUnitaireProd=10.0
                                                   )
        self.rn = Rayon.objects.create(nomRayon="RayonPourTest")
        self.ctnr = Contenir.objects.create(produit=self.prod, rayon=self.rn, Qte=1)

    def test_contenir_creation(self):
        self.assertEqual(self.ctnr.produit.intituleProd, "ProdTest")
        

    def test_string_representation(self):
        self.assertEqual(str(self.ctnr), "ProdTest dans RayonPourTest (Qte: 1)")

    def test_contenir_updating(self):
        self.ctnr.produit.intituleProd = "prodCntrModif"
        self.ctnr.produit.save()
        # Récup obj maj
        updated_ctnr = Contenir.objects.get(produit=self.ctnr.produit)
        self.assertEqual(updated_ctnr.produit.intituleProd, "prodCntrModif")

    def test_contenir_deletion(self):
        self.ctnr.delete()
        self.assertEqual(Contenir.objects.count(),0)