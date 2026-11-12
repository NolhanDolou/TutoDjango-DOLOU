from datetime import date
from unittest import TestCase
from monApp.models import Produit
from monApp.forms import ProduitForm


class ProduitFormTest(TestCase):

    def setUp(self) :
        self.produit = Produit.objects.create(intituleProd="ProduitPourTestFormulaire",
        prixUnitaireProd=10.0,dateFabProd= date(2023, 1, 1),categorie=None,statut=None)
    
    # test du champ intituleProd trop long
    def test_form_valid_data_too_long(self):
        data = {"intituleProd": self.produit.intituleProd*10,
        "prixUnitaireProd":self.produit.prixUnitaireProd,
        "dateFabProd":self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Assurez-vous que cette valeur comporte au plus 200 caractères (actuellement 250).'])
        
    # test du champ intituleProd manquant    
    def test_form_valid_data_missed(self):
        data = {"intituleProd": "",
        "prixUnitaireProd":self.produit.prixUnitaireProd,
        "dateFabProd":self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Ce champ est obligatoire.'])


    def test_form_valid_and_save(self):
        data = {"intituleProd": self.produit.intituleProd,
        "prixUnitaireProd":self.produit.prixUnitaireProd,
        "dateFabProd":self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertTrue(form.is_valid())
        prdt = form.save()
        self.assertEqual(prdt.intituleProd, 'ProduitPourTestFormulaire')

