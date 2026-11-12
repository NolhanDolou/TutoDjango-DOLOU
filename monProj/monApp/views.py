from django.shortcuts import render
from monApp.models import Produit
from monApp.models import Categorie
from monApp.models import Rayon
from monApp.models import Statut
from django.http import Http404
from django.views.generic import *
from django import forms
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.forms import BaseModelForm






# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from monApp.forms import ContactUsForm
from monApp.forms import ProduitForm
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['param'] = "Hello Django!"
        new_param = self.kwargs.get('param')
        context['page'] = "home"
        if new_param!=None : 
            context['param'] = "Hello " + new_param + "!"
        
        return context
        

# class ContactView(TemplateView):
#     template_name = "monApp/home.html"
    
#     def get_context_data(self, **kwargs):
#         context = super(ContactView, self).get_context_data(**kwargs)
#         context['param'] = "Hello Django!"
#         context['page'] = "contact"
#         return context
    
class ContactView(FormView):
    template_name = "monApp/home.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("email-sent")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Contact Us"
        return context
    def form_valid(self, form):
        send_mail(
        subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MonProjet Contact Us form',
        message=form.cleaned_data["message"],
        from_email=form.cleaned_data["email"],
        recipient_list=["admin@monprojet.com"],
        )
        return super().form_valid(form)


def EmailSentView(request):
    return render(
        request,
        "monApp/home.html",
        {"message": "Votre message a bien été envoyé."},
    )

class AboutView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['param'] = "Hello Django!"
        context['page'] = "about"
        return context

# ---------------------------------------------------------------
# ------------------ LES LISTES ---------------------------------

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "produits"

    def get_queryset(self):
        return Produit.objects.order_by("prixUnitaireProd") # tri sur le prix

    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits !"
        return context

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context

class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/ListCategories.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Categories !"
        return context
    

class CategorieDetailView(DetailView): 
    model = Categorie
    template_name = "monApp/detail_categorie.html" 
    context_object_name = "ctr"

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/ListRayons.html"
    context_object_name = "rayons"

    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons !"
        return context
    

class RayonDetailView(DetailView): 
    model = Rayon
    template_name = "monApp/detail_rayon.html" 
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context

class StatutListView(ListView):
    model = Statut
    template_name = "monApp/ListStatuts.html"
    context_object_name = "statuts"

    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes statuts !"
        return context
    

class StatutDetailView(DetailView): 
    model = Statut
    template_name = "monApp/detail_statut.html" 
    context_object_name = "stt"

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        return context


class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"

    def get_context_data(self,**kwargs):
        context = super(ProduitCreateView, self).get_context_data(**kwargs)
        context['titremenu'] = "Ajout d'un nouveau produit"
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('detailProduit', prdt.refProd)


class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"

    def get_context_data(self,**kwargs):
        context = super(ProduitUpdateView, self).get_context_data(**kwargs)
        context['titremenu'] = "Modification du produit"
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('detailProduit', prdt.refProd)
