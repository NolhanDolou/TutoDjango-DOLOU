from django.test import TestCase
from monApp.models import Statut

class StatutModelTest(TestCase):
    def setUp(self):
        # créer attribut statut a utiliser dans les tests
        self.stt = Statut.objects.create(libelleStatut="StatutTest")

    def test_statut_creation(self):
        self.assertEqual(self.stt.libelleStatut, "StatutTest")

    def test_string_representation(self):
        self.assertEqual(str(self.stt), "StatutTest")

    def test_statut_updating(self):
        self.stt.libelleStatut = "StatutTestModifie"
        self.stt.save()
        # Récup obj maj
        updated_stt = Statut.objects.get(idStatut=self.stt.idStatut)
        self.assertEqual(updated_stt.libelleStatut, "StatutTestModifie")

    def test_categorie_deletion(self):
        self.stt.delete()
        self.assertEqual(Statut.objects.count(),0)