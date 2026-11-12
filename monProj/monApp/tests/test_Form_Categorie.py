from django.test import TestCase

from monApp.forms import CategorieForm
from monApp.models import Categorie


class CategorieFormTest(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(
            nomCat="CategoriePourTestFormulaire",
        )

    # test du champ nomCat trop long
    def test_form_valid_data_too_long(self):
        data = {
            "nomCat": self.categorie.nomCat * 10,
        }
        form = CategorieForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('nomCat', form.errors)  # Le champ 'nomCat' doit contenir une erreur
        self.assertEqual(form.errors['nomCat'], ['Assurez-vous que cette valeur comporte au plus 100 caractères (actuellement 270).'])

    # test du champ nomCat manquant
    def test_form_valid_data_missed(self):
        data = {
            "nomCat": "",
        }
        form = CategorieForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('nomCat', form.errors)  # Le champ 'nomCat' doit contenir une erreur
        self.assertEqual(form.errors['nomCat'], ['Ce champ est obligatoire.'])

    # test du formulaire valide
    def test_form_valid_and_save(self):
        data = {
            "nomCat": self.categorie.nomCat,
        }
        form = CategorieForm(data)
        self.assertTrue(form.is_valid())
        categorie = form.save()
        self.assertEqual(categorie.nomCat, 'CategoriePourTestFormulaire')
