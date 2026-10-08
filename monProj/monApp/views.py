from django.shortcuts import render
from monApp.models import Produit
from monApp.models import Categorie
from monApp.models import Rayon
from monApp.models import Statut
from django.http import Http404
from django.views.generic import *




# Create your views here.
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['param'] = "Hello Django!"
        new_param = self.kwargs.get('param')
        if new_param!=None : 
            context['param'] = "Hello " + new_param + "!"
        
        return context
        

class ContactView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['param'] = "Hello Django!"
        context['page'] = "contact"
        return context
    

class AboutView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['param'] = "Hello Django!"
        context['page'] = "about"
        return context

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