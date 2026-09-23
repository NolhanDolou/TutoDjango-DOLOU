from django.test import TestCase
from monApp.models import Rayon

class RayonModelTest(TestCase):
    def setUp(self):
        # créer attribut produit a utiliser dans les tests
        self.rn = Rayon.objects.create(nomRayon="RayonPourTest")

    def test_rayon_creation(self):
        self.assertEqual(self.rn.nomRayon, "RayonPourTest")

    def test_string_representation(self):
        self.assertEqual(str(self.rn), "RayonPourTest")

    def test_rayon_updating(self):
        self.rn.nomRayon = "RayonPourTestsModifiee"
        self.rn.save()
        # Récup obj maj
        updated_rn = Rayon.objects.get(idRayon=self.rn.idRayon)
        self.assertEqual(updated_rn.nomRayon, "RayonPourTestsModifiee")

    def test_rayon_deletion(self):
        self.rn.delete()
        self.assertEqual(Rayon.objects.count(),0)