from django.contrib import admin
from .models import Produit, Categorie, Statut, Rayon

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    model=Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "dateFabProd", "categorie", "statut"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateFabProd"]
    radio_fields = {"statut": admin.VERTICAL}



class ProduitInline(admin.TabularInline):
    model=Produit
    extra=1 #nb lignes vides par defaut

class CategorieAdmin(admin.ModelAdmin):
    model=Categorie
    inlines=[ProduitInline]


admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Statut)
admin.site.register(Rayon)