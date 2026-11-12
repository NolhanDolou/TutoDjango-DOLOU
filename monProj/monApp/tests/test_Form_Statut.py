from django.test import TestCase

from monApp.forms import StatutForm
from monApp.models import Statut


class StatutFormTest(TestCase):

    def setUp(self):
        self.statut = Statut.objects.create(
            libelleStatut="StatutPourTestFormulaire",
        )

    # test du champ libelleStatut trop long
    def test_form_valid_data_too_long(self):
        data = {
            "libelleStatut": self.statut.libelleStatut * 10,
        }
        form = StatutForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('libelleStatut', form.errors)  # Le champ 'libelleStatut' doit contenir une erreur
        self.assertEqual(form.errors['libelleStatut'], ['Assurez-vous que cette valeur comporte au plus 100 caractères (actuellement 240).'])

    # test du champ libelleStatut manquant
    def test_form_valid_data_missed(self):
        data = {
            "libelleStatut": "",
        }
        form = StatutForm(data)
        self.assertFalse(form.is_valid())  # Le formulaire doit être invalide
        self.assertIn('libelleStatut', form.errors)  # Le champ 'libelleStatut' doit contenir une erreur
        self.assertEqual(form.errors['libelleStatut'], ['Ce champ est obligatoire.'])

    # test du formulaire valide
    def test_form_valid_and_save(self):
        data = {
            "libelleStatut": self.statut.libelleStatut,
        }
        form = StatutForm(data)
        self.assertTrue(form.is_valid())
        statut = form.save()
        self.assertEqual(statut.libelleStatut, 'StatutPourTestFormulaire')
