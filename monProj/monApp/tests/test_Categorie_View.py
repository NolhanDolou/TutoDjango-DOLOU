from django.test import TestCase
from django.urls import reverse

from monApp.models import Categorie


class CategorieCreateViewTest(TestCase):
    def test_categorie_create_view_post_valid(self):
        data = {
            "nomCat": "CategoriePourTestCreation",
        }
        # simulation soumission formulaire
        response = self.client.post(reverse('creationCategorie'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Categorie.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Categorie.objects.last().nomCat, 'CategoriePourTestCreation')


class CategorieUpdateViewTest(TestCase):
    def test_categorie_update_view_get(self):
        categorie = Categorie.objects.create(nomCat="CategorieAvantModification")
        response = self.client.get(reverse('modificationCategorie', args=[categorie.pk]))
        self.assertEqual(response.status_code, 200)

    def test_categorie_update_view_post_valid(self):
        categorie = Categorie.objects.create(nomCat="CategorieAvantModification")
        data = {
            "nomCat": "CategorieApresModification",
        }
        response = self.client.post(reverse('modificationCategorie', args=[categorie.pk]), data)
        self.assertEqual(response.status_code, 302)
        categorie.refresh_from_db()
        self.assertEqual(categorie.nomCat, 'CategorieApresModification')


class CategorieDeleteViewTest(TestCase):
    def test_categorie_delete_view_get(self):
        categorie = Categorie.objects.create(nomCat="CategoriePourSuppression")
        response = self.client.get(reverse('suppressionCategorie', args=[categorie.pk]))
        self.assertEqual(response.status_code, 200)

    def test_categorie_delete_view_post_valid(self):
        categorie = Categorie.objects.create(nomCat="CategoriePourSuppression")
        response = self.client.post(reverse('suppressionCategorie', args=[categorie.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Categorie.objects.count(), 0)
