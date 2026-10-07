from django.shortcuts import render
from monApp.models import Produit
from monApp.models import Categorie
from monApp.models import Rayon
from monApp.models import Statut
from django.http import Http404
from django.views.generic import *




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

# def home(request,param=None):
#     return render(request, 'monApp/home.html', {'param':param})

class HomeView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['param'] = "Hello Django!"
        return context
    

# def contact(request):
#     return HttpResponse("<h1>Bienvenue sur la page de contact</h1>")

class ContactView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['param'] = "Hello Django!"
        context['page'] = "contact"
        return context
    


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


# def ListeCategories(request):
#     cate = Categorie.objects.all()
#     res = "<ul>"
#     for cat in cate:
#         res += f"<li>{cat.nomCat}</li>"
#     res += "</ul>"
#     return HttpResponse(res)

def ListeCategories(request):
    categories = Categorie.objects.all()
    return render(request, "monApp/ListCategories.html", {'categories':categories})

# def ListeRayons(request):
#     rayon = Rayon.objects.all()
#     res = "<ul>"
#     for rn in rayon:
#         res += f"<li>{rn.nomRayon}</li>"
#     res += "</ul>"
#     return HttpResponse(res)

def ListeRayons(request):
    rayons = Rayon.objects.all()
    return render(request, "monApp/ListRayons.html", {'rayons':rayons})

# def ListeStatuts(request):
#     statut = Statut.objects.all()
#     res = "<ul>"
#     for st in statut:
#         res += f"<li>{st.libelleStatut}</li>"
#     res += "</ul>"
#     return HttpResponse(res)

def ListeStatuts(request):
    statuts = Statut.objects.all()
    return render(request, "monApp/ListStatuts.html", {'statuts':statuts})