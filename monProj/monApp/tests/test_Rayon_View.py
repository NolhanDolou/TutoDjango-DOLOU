from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from monApp.models import Rayon


class RayonCreateViewTest(TestCase):
    def setUp(self):
        # connexion d'un utilisateur : ces vues exigent maintenant l'authentification
        self.user = User.objects.create_user("testeur", "testeur@example.com", "MotDePasse123")
        self.client.force_login(self.user)

    def test_rayon_create_view_post_valid(self):
        data = {
            "nomRayon": "RayonPourTestCreation",
        }
        # simulation soumission formulaire
        response = self.client.post(reverse('creationRayon'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Rayon.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Rayon.objects.last().nomRayon, 'RayonPourTestCreation')


class RayonUpdateViewTest(TestCase):
    def setUp(self):
        # connexion d'un utilisateur : ces vues exigent maintenant l'authentification
        self.user = User.objects.create_user("testeur", "testeur@example.com", "MotDePasse123")
        self.client.force_login(self.user)

    def test_rayon_update_view_get(self):
        rayon = Rayon.objects.create(nomRayon="RayonAvantModification")
        response = self.client.get(reverse('modificationRayon', args=[rayon.pk]))
        self.assertEqual(response.status_code, 200)

    def test_rayon_update_view_post_valid(self):
        rayon = Rayon.objects.create(nomRayon="RayonAvantModification")
        data = {
            "nomRayon": "RayonApresModification",
        }
        response = self.client.post(reverse('modificationRayon', args=[rayon.pk]), data)
        self.assertEqual(response.status_code, 302)
        rayon.refresh_from_db()
        self.assertEqual(rayon.nomRayon, 'RayonApresModification')


class RayonDeleteViewTest(TestCase):
    def setUp(self):
        # connexion d'un utilisateur : ces vues exigent maintenant l'authentification
        self.user = User.objects.create_user("testeur", "testeur@example.com", "MotDePasse123")
        self.client.force_login(self.user)

    def test_rayon_delete_view_get(self):
        rayon = Rayon.objects.create(nomRayon="RayonPourSuppression")
        response = self.client.get(reverse('suppressionRayon', args=[rayon.pk]))
        self.assertEqual(response.status_code, 200)

    def test_rayon_delete_view_post_valid(self):
        rayon = Rayon.objects.create(nomRayon="RayonPourSuppression")
        response = self.client.post(reverse('suppressionRayon', args=[rayon.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Rayon.objects.count(), 0)