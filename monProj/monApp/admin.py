from decimal import ROUND_HALF_UP, Decimal

from django.contrib import admin
from .models import Produit, Categorie, Statut, Rayon, Contenir

# Register your models here.

class ProduitFilter(admin.SimpleListFilter):
    title='filtre produit'
    parameter_name='custom_statut'

    def lookups(self, request, model_admin):
        return (
            ('OnLine', 'En ligne'),
            ('OffLine', 'Hors ligne'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'OnLine':
            return queryset.filter(statut=1)
        if self.value() == 'OffLine':
            return queryset.filter(statut=0)

def set_Produit_online(modeladmin, request, queryset):
    queryset.update(statut=1)
set_Produit_online.short_description = "Mettre en ligne"

def set_Produit_offline(modeladmin, request, queryset):
    queryset.update(statut=0)
set_Produit_offline.short_description = "Mettre hors ligne"


class ContenirProduitInline(admin.TabularInline):
    model = Contenir
    fields = ("rayon", "Qte")
    extra = 1


class ContenirRayonInline(admin.TabularInline):
    model = Contenir
    fields = ("produit", "Qte")
    extra = 1


class ProduitAdmin(admin.ModelAdmin):
    model=Produit
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "prixTTCProd", "dateFabProd", "categorie", "statut"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateFabProd"]
    radio_fields = {"statut": admin.VERTICAL}
    search_fields = ('intituleProd', 'dateFabProd')
    list_filter = (ProduitFilter,)
    date_hierarchy = 'dateFabProd'
    ordering = ('-dateFabProd',)
    actions = [set_Produit_online, set_Produit_offline]
    inlines = [ContenirProduitInline]

    def prixTTCProd(self, instance):
        return (instance.prixUnitaireProd * Decimal('1.20')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    prixTTCProd.short_description = "Prix TTC"
    prixTTCProd.admin_order_field = "prixUnitaireProd"




class ProduitInline(admin.TabularInline):
    model=Produit
    extra=1 #nb lignes vides par defaut


class RayonAdmin(admin.ModelAdmin):
    model = Rayon
    list_display = ("idRayon", "nomRayon")
    search_fields = ("nomRayon",)
    inlines = [ContenirRayonInline]

class CategorieAdmin(admin.ModelAdmin):
    model=Categorie
    inlines=[ProduitInline]


class ContenirAdmin(admin.ModelAdmin):
    list_display = ("produit", "rayon", "Qte")
    list_filter = ("rayon", "produit")
    search_fields = ("produit__intituleProd", "rayon__nomRayon")


admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Statut)
admin.site.register(Rayon, RayonAdmin)
admin.site.register(Contenir, ContenirAdmin)