from django.shortcuts import render
from monApp.models import Produit
from monApp.models import Categorie
from monApp.models import Rayon
from monApp.models import Statut
from django.http import Http404



# Create your views here.
from django.http import HttpResponse

# # Ma première version
# def home(request, param="default"):
#     print(request.__dict__)
#     return HttpResponse(f"<h1>Hello {param}!</h1>")

# def home(request, param=None):
#     if request.GET:
#         if 'name' in request.GET:                                                                                                   
#             string = request.GET['name']
#             return HttpResponse("Bonjour %s!" % string)     
#         if 'test' in request.GET:
#             raise Http404       
#     if param:
#         return HttpResponse(f"<h1>Hello {param}!</h1>")
#     return HttpResponse("<h1>Hello Django!</h1>")

# def home(request,param=None):
#     if param:
#         return HttpResponse(f"<h1>Hello {param}!</h1>")
#     return HttpResponse("<h1>Hello Django!</h1>")

def home(request,param=None):
    return render(request, 'monApp/home.html', {'param':param})
    

# def contact(request):
#     return HttpResponse("<h1>Bienvenue sur la page de contact</h1>")


def contact(request):
    return render(request, "monApp/contact.html")


# def aboutus(request):
#     return HttpResponse("<h1>Bienvenue sur la page d'infomations</h1>")

def aboutus(request):
    return render(request, "monApp/about.html")

# def ListeProduits(request):
#     prdts = Produit.objects.all()
#     res = "<ul>"
#     for prd in prdts:
#         res += f"<li>{prd.intituleProd}</li>"
#     res += "</ul>"
#     return HttpResponse(res)

# Nouvelle version : 
def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html', {'produits':prdts})


def ListeCategories(request):
    cate = Categorie.objects.all()
    res = "<ul>"
    for cat in cate:
        res += f"<li>{cat.nomCat}</li>"
    res += "</ul>"
    return HttpResponse(res)

def ListeRayons(request):
    rayon = Rayon.objects.all()
    res = "<ul>"
    for rn in rayon:
        res += f"<li>{rn.nomRayon}</li>"
    res += "</ul>"
    return HttpResponse(res)

def ListeStatuts(request):
    statut = Statut.objects.all()
    res = "<ul>"
    for st in statut:
        res += f"<li>{st.libelleStatut}</li>"
    res += "</ul>"
    return HttpResponse(res)