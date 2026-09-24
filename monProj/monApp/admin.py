from django.contrib import admin
from .models import Produit

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    list_display=('intituleProd', 'prixUnitaireProd')
admin.site.register(Produit, ProduitAdmin)