from django.shortcuts import render
from monApp.models import Produit


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

def ListeProduits(request):
    prdts = Produit.objects.all()
    res = "<ul>"
    for prd in prdts:
        res += f"<li>{prd.intituleProd}</li>"
    res += "</ul>"
    return HttpResponse(res)