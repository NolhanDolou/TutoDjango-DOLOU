from django.shortcuts import render
from monApp.models import Produit
from monApp.models import Categorie
from monApp.models import Rayon
from monApp.models import Statut


# Create your views here.
from django.http import HttpResponse
def home(request, param="default"):
    return HttpResponse(f"<h1>Hello {param}!</h1>")


def contact(request):
    return HttpResponse("<h1>Bienvenue sur la page de contact</h1>")

def aboutus(request):
    return HttpResponse("<h1>Bienvenue sur la page d'infomations</h1>")

def ListeProduits(request):
    prdts = Produit.objects.all()
    res = "<ul>"
    for prd in prdts:
        res += f"<li>{prd.intituleProd}</li>"
    res += "</ul>"
    return HttpResponse(res)

def ListeCategories(request):
    cate = Categorie.objects.all()
    res = "<ul>"
    for cat in cate:
        res += f"<li>{cat.nomCat}</li>"
    res += "</ul>"
    return HttpResponse(res)

