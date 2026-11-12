from django.test import TestCase
from django.urls import reverse
from monApp.models import Produit, Categorie, Rayon, Statut

class ListViewTest(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(nomCat="Boissons")
        self.rayon = Rayon.objects.create(nomRayon="Rayon A")
        self.statut = Statut.objects.create(libelleStatut="Disponible")
        self.produit = Produit.objects.create(
            intituleProd="Coca-Cola",
            prixUnitaireProd=1.50,
            categorie=self.categorie,
            statut=self.statut,
        )


    # test de l'url de la page d'accueil
    def test_lst_prod_status_code(self):
        response = self.client.get(reverse('listProduits'))
        self.assertEqual(response.status_code, 200)

    def test_lst_cate_status_code(self):
        response = self.client.get(reverse('ListeCategories'))
        self.assertEqual(response.status_code, 200)

    def test_lst_rn_status_code(self):
        response = self.client.get(reverse('ListeRayons'))
        self.assertEqual(response.status_code, 200)

    def test_lst_stt_status_code(self):
        response = self.client.get(reverse('ListeStatuts'))
        self.assertEqual(response.status_code, 200)


#----------------------------------------------------------------------------------

    def test_liste_produits_content(self):
        response = self.client.get(reverse('listProduits'))
        self.assertContains(response, f"<td>{self.produit.intituleProd} </td>")

    def test_liste_categories_content(self):
        response = self.client.get(reverse('ListeCategories'))
        self.assertContains(response, f"<td>{self.categorie.nomCat} </td>")
        self.assertContains(response, "<td>1 </td>")

    def test_liste_statuts_affiche_nombre_produits(self):
        response = self.client.get(reverse('ListeStatuts'))

        self.assertContains(response, f"<td>{self.statut.libelleStatut} </td>")
        self.assertContains(response, "<td>1 </td>")
        self.assertEqual(response.context["statuts"][0].nb_produits, 1)

    def test_detail_statut_affiche_nombre_et_produits(self):
        response = self.client.get(
            reverse("detailStatut", args=[self.statut.pk])
        )

        self.assertContains(response, "Ce statut contient")
        self.assertContains(response, self.produit.intituleProd)
        self.assertContains(
            response,
            reverse("detailProduit", args=[self.produit.pk]),
        )
        self.assertEqual(response.context["stt"].nb_produits, 1)
        self.assertQuerySetEqual(
            response.context["produits"],
            [self.produit],
        )

    def test_detail_statut_sans_produits_affiche_message(self):
        statut_sans_produit = Statut.objects.create(libelleStatut="Indisponible")

        response = self.client.get(
            reverse("detailStatut", args=[statut_sans_produit.pk])
        )

        self.assertContains(
            response,
            "Aucun produit trouvé pour ce statut.",
        )
        self.assertEqual(response.context["stt"].nb_produits, 0)
        self.assertQuerySetEqual(response.context["produits"], [])

    def test_detail_categorie_affiche_nombre_produits(self):
        response = self.client.get(
            reverse("detailCategorie", args=[self.categorie.pk])
        )

        self.assertContains(response, "Cette catégorie contient")
        self.assertEqual(response.context["ctr"].nb_produits, 1)
        self.assertContains(response, self.produit.intituleProd)

    def test_liste_rayons_content(self):
        response = self.client.get(reverse('ListeRayons'))
        self.assertContains(response, f"<td>{self.rayon.nomRayon} </td>")

    def test_liste_statuts_content(self):
        response = self.client.get(reverse('ListeStatuts'))
        self.assertContains(response, f"<td>{self.statut.libelleStatut} </td>")