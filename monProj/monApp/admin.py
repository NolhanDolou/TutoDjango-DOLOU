from django.contrib import admin
from .models import Produit, Categorie, Statut, Rayon

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    list_display=('intituleProd', 'prixUnitaireProd')

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie)
admin.site.register(Statut)
admin.site.register(Rayon)