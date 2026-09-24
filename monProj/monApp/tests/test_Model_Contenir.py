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
        

    # def test_string_representation(self):
    #     self.assertEqual(str(self.ctgr), "ContenuePourTest")

    # def test_categorie_updating(self):
    #     self.ctgr.nomCat = "CategoriePourTestsModifiee"
    #     self.ctgr.save()
    #     # Récup obj maj
    #     updated_ctgr = Categorie.objects.get(idCat=self.ctgr.idCat)
    #     self.assertEqual(updated_ctgr.nomCat, "CategoriePourTestsModifiee")

    # def test_categorie_deletion(self):
    #     self.ctgr.delete()
    #     self.assertEqual(Categorie.objects.count(),0)