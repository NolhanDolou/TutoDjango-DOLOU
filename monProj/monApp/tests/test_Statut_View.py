from django.test import TestCase
from django.urls import reverse

from monApp.models import Statut


class StatutCreateViewTest(TestCase):
    def test_statut_create_view_post_valid(self):
        data = {
            "libelleStatut": "StatutPourTestCreation",
        }
        # simulation soumission formulaire
        response = self.client.post(reverse('creationStatut'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Statut.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Statut.objects.last().libelleStatut, 'StatutPourTestCreation')


class StatutUpdateViewTest(TestCase):
    def test_statut_update_view_get(self):
        statut = Statut.objects.create(libelleStatut="StatutAvantModification")
        response = self.client.get(reverse('modificationStatut', args=[statut.pk]))
        self.assertEqual(response.status_code, 200)

    def test_statut_update_view_post_valid(self):
        statut = Statut.objects.create(libelleStatut="StatutAvantModification")
        data = {
            "libelleStatut": "StatutApresModification",
        }
        response = self.client.post(reverse('modificationStatut', args=[statut.pk]), data)
        self.assertEqual(response.status_code, 302)
        statut.refresh_from_db()
        self.assertEqual(statut.libelleStatut, 'StatutApresModification')


class StatutDeleteViewTest(TestCase):
    def test_statut_delete_view_get(self):
        statut = Statut.objects.create(libelleStatut="StatutPourSuppression")
        response = self.client.get(reverse('suppressionStatut', args=[statut.pk]))
        self.assertEqual(response.status_code, 200)

    def test_statut_delete_view_post_valid(self):
        statut = Statut.objects.create(libelleStatut="StatutPourSuppression")
        response = self.client.post(reverse('suppressionStatut', args=[statut.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Statut.objects.count(), 0)
