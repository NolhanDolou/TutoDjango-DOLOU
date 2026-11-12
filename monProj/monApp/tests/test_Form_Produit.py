from datetime import date
from decimal import Decimal

from django.test import TestCase

from monApp.forms import ProduitForm
from monApp.models import Produit


class ProduitFormTest(TestCase):

    def setUp(self):
        self.produit = Produit.objects.create(
            intituleProd="ProduitPourTestFormulaire",
            prixUnitaireProd=10.0,
            dateFabProd=date(2023, 1, 1),
            categorie=None,
            statut=None,
        )

    # test du champ intituleProd trop long
    def test_form_valid_data_too_long(self):
        data = {
            "intituleProd": self.produit.intituleProd * 10,
            "prixUnitaireProd": self.produit.prixUnitaireProd,
            "dateFabProd": self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors)  # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Assurez-vous que cette valeur comporte au plus 200 caractères (actuellement 250).'])

    # test du champ intituleProd manquant
    def test_form_valid_data_missed(self):
        data = {
            "intituleProd": "",
            "prixUnitaireProd": self.produit.prixUnitaireProd,
            "dateFabProd": self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors)  # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Ce champ est obligatoire.'])

    # test du formulaire valide
    def test_form_valid_and_save(self):
        data = {
            "intituleProd": self.produit.intituleProd,
            "prixUnitaireProd": self.produit.prixUnitaireProd,
            "dateFabProd": self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertTrue(form.is_valid())
        prdt = form.save()
        self.assertEqual(prdt.intituleProd, 'ProduitPourTestFormulaire')

    # test du champ prixUnitaireProd manquant
    def test_form_prix_data_missed(self):
        data = {
            "intituleProd": self.produit.intituleProd,
            "prixUnitaireProd": "",
            "dateFabProd": self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('prixUnitaireProd', form.errors)  # Le champ 'prixUnitaireProd' doit contenir une erreur
        self.assertEqual(form.errors['prixUnitaireProd'], ['Ce champ est obligatoire.'])

    # test du champ prixUnitaireProd qui n'est pas un nombre
    def test_form_prix_not_a_number(self):
        data = {
            "intituleProd": self.produit.intituleProd,
            "prixUnitaireProd": "abc",
            "dateFabProd": self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('prixUnitaireProd', form.errors)
        self.assertEqual(form.errors['prixUnitaireProd'], ['Saisissez un nombre.'])

    # test du champ prixUnitaireProd avec trop de chiffres au total (11 > 10)
    def test_form_prix_too_many_digits(self):
        data = {
            "intituleProd": self.produit.intituleProd,
            "prixUnitaireProd": "123456789.12",
            "dateFabProd": self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('prixUnitaireProd', form.errors)
        self.assertEqual(form.errors['prixUnitaireProd'], ["Assurez-vous qu’il n’y a pas plus de 10 chiffres au total."])

    # test du champ prixUnitaireProd avec trop de décimales (3 > 2)
    def test_form_prix_too_many_decimals(self):
        data = {
            "intituleProd": self.produit.intituleProd,
            "prixUnitaireProd": "10.123",
            "dateFabProd": self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('prixUnitaireProd', form.errors)
        self.assertEqual(form.errors['prixUnitaireProd'], ["Assurez-vous qu’il n’y a pas plus de 2 chiffres après la virgule."])

    # test du champ prixUnitaireProd valide avec 2 décimales
    def test_form_prix_valid_and_save(self):
        data = {
            "intituleProd": self.produit.intituleProd,
            "prixUnitaireProd": "99.99",
            "dateFabProd": self.produit.dateFabProd,
        }
        form = ProduitForm(data)
        self.assertTrue(form.is_valid())
        prdt = form.save()
        self.assertEqual(prdt.prixUnitaireProd, Decimal('99.99'))