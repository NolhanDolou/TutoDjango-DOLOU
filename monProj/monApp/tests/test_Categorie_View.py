from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from monApp.models import Categorie


class CategorieViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testeur", "testeur@example.com", "MotDePasse123"
        )
        self.client.force_login(self.user)


class CategorieCreateViewTest(CategorieViewTestCase):
    def test_categorie_create_view_post_valid(self):
        response = self.client.post(
            reverse("creationCategorie"),
            {"nomCat": "CategoriePourTestCreation"},
        )

        self.assertEqual(response.status_code, 302)
        categorie = Categorie.objects.get(nomCat="CategoriePourTestCreation")
        self.assertRedirects(
            response, reverse("detailCategorie", args=[categorie.idCat])
        )


class CategorieUpdateViewTest(CategorieViewTestCase):
    def setUp(self):
        super().setUp()
        self.categorie = Categorie.objects.create(
            nomCat="CategorieAvantModification"
        )

    def test_categorie_update_view_get_context(self):
        response = self.client.get(
            reverse("modificationCategorie", args=[self.categorie.idCat])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["titremenu"], "Modification de la catégorie"
        )

    def test_categorie_update_view_post_valid(self):
        response = self.client.post(
            reverse("modificationCategorie", args=[self.categorie.idCat]),
            {"nomCat": "CategorieApresModification"},
        )

        self.assertEqual(response.status_code, 302)
        self.categorie.refresh_from_db()
        self.assertEqual(self.categorie.nomCat, "CategorieApresModification")
        self.assertRedirects(
            response, reverse("detailCategorie", args=[self.categorie.idCat])
        )


class CategorieDeleteViewTest(CategorieViewTestCase):
    def test_categorie_delete_view_post_valid(self):
        categorie = Categorie.objects.create(nomCat="CategoriePourSuppression")

        response = self.client.post(
            reverse("suppressionCategorie", args=[categorie.idCat])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Categorie.objects.filter(pk=categorie.idCat).exists())
