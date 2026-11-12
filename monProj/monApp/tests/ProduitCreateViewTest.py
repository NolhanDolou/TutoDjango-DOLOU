def test_categorie_create_view_post_valid(self):
    data = { "intituleProd": "ProduitPourTestCreation",
        "prixUnitaireProd":100.0,
        "dateFabProd":date(2023, 1, 1),
        "categorie":"",
        "statut":"" }
    #simulation soumission formulaire
    response = self.client.post(reverse('creationProduit'), data)
    # Vérifie la redirection après la création
    self.assertEqual(response.status_code, 302)
    # Vérifie qu'un objet a été créé
    self.assertEqual(Produit.objects.count(), 1)
    # Vérifie la valeur de l'objet créé
    self.assertEqual(Produit.objects.last().intituleProd, 'ProduitPourTestCreation')