from django.test import TestCase

from monApp.forms import RayonForm
from monApp.models import Rayon


class RayonFormTest(TestCase):

    def setUp(self):
        self.rayon = Rayon.objects.create(
            nomRayon="RayonPourTestFormulaire",
        )

    # test du champ nomRayon trop long
    def test_form_valid_data_too_long(self):
        data = {
            "nomRayon": self.rayon.nomRayon * 10,
        }
        form = RayonForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('nomRayon', form.errors)  # Le champ 'nomRayon' doit contenir une erreur
        self.assertEqual(form.errors['nomRayon'], ['Assurez-vous que cette valeur comporte au plus 100 caractères (actuellement 230).'])

    # test du champ nomRayon manquant
    def test_form_valid_data_missed(self):
        data = {
            "nomRayon": "",
        }
        form = RayonForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('nomRayon', form.errors)  # Le champ 'nomRayon' doit contenir une erreur
        self.assertEqual(form.errors['nomRayon'], ['Ce champ est obligatoire.'])

    # test du formulaire valide
    def test_form_valid_and_save(self):
        data = {
            "nomRayon": self.rayon.nomRayon,
        }
        form = RayonForm(data)
        self.assertTrue(form.is_valid())
        rayon = form.save()
        self.assertEqual(rayon.nomRayon, 'RayonPourTestFormulaire')
