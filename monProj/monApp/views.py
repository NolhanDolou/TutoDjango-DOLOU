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
from django.db.models import Count, Prefetch
from monApp.models import Contenir


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from monApp.forms import ContactUsForm
from monApp.forms import ProduitForm
from monApp.forms import CategorieForm
from monApp.forms import RayonForm
from monApp.forms import StatutForm
from monApp.forms import ContenirForm
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
        # Charge les catégories et les statuts en même temps
        queryset = Produit.objects.select_related('categorie').select_related('statut')
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(intituleProd__icontains=query)
        return queryset

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

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        queryset = Categorie.objects.annotate(nb_produits=Count('produit_categorie'))
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(nomCat__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Categories !"
        return context
    

class CategorieDetailView(DetailView): 
    model = Categorie
    template_name = "monApp/detail_categorie.html" 
    context_object_name = "ctr"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produit_categorie'))

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['produits'] = self.object.produit_categorie.all()
        return context

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/ListRayons.html"
    context_object_name = "rayons"

    def get_queryset(self):
        # Précharge tous les "contenir" de chaque rayon,
        # et en même temps le produit de chaque contenir
        queryset = Rayon.objects.prefetch_related(
            Prefetch("contenir_rayon", queryset=Contenir.objects.select_related("produit"))
        )
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(nomRayon__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons !"
        rayons_data = []
        for rayon in context['rayons']:
            total = 0
            for contenir in rayon.contenir_rayon.all():
                total += contenir.produit.prixUnitaireProd * contenir.Qte
            rayons_data.append({'rayon': rayon,'total_stock': total})
        context['rayons_data'] = rayons_data
        return context
    

class RayonDetailView(DetailView): 
    model = Rayon
    template_name = "monApp/detail_rayon.html" 
    context_object_name = "rayon"

    def get_queryset(self):
        return Rayon.objects.prefetch_related(
            Prefetch(
                "contenir_rayon",
                queryset=Contenir.objects.select_related("produit"),
            )
        )

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"

        produits_data = []
        total_rayon = 0
        total_nb_produit = 0

        for contenir in self.object.contenir_rayon.all():
            total_produit = contenir.produit.prixUnitaireProd * contenir.Qte
            produits_data.append({'produit': contenir.produit,
                'qte': contenir.Qte,
                'prix_unitaire': contenir.produit.prixUnitaireProd,
                'total_produit': total_produit} )
            total_rayon += total_produit
            total_nb_produit += contenir.Qte
        context['produits_data'] = produits_data
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit
        return context

class StatutListView(ListView):
    model = Statut
    template_name = "monApp/ListStatuts.html"
    context_object_name = "statuts"

    def get_queryset(self):
        queryset = Statut.objects.annotate(nb_produits=Count('produit_statut'))
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(libelleStatut__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes statuts !"
        return context
    

class StatutDetailView(DetailView): 
    model = Statut
    template_name = "monApp/detail_statut.html" 
    context_object_name = "stt"

    def get_queryset(self):
        return Statut.objects.annotate(nb_produits=Count('produit_statut'))

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        context['produits'] = self.object.produit_statut.all()
        return context


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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



@method_decorator(login_required, name='dispatch')
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('listProduits')


@method_decorator(login_required, name='dispatch')
class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/create_categorie.html"

    def get_context_data(self, **kwargs):
        context = super(CategorieCreateView, self).get_context_data(**kwargs)
        context['titremenu'] = "Ajout d'une nouvelle catégorie"
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        categorie = form.save()
        return redirect('detailCategorie', categorie.idCat)


@method_decorator(login_required, name='dispatch')
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/update_categorie.html"

    def get_context_data(self, **kwargs):
        context = super(CategorieUpdateView, self).get_context_data(**kwargs)
        context['titremenu'] = "Modification de la catégorie"
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        categorie = form.save()
        return redirect('detailCategorie', categorie.idCat)


@method_decorator(login_required, name='dispatch')
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('ListeCategories')


@method_decorator(login_required, name='dispatch')
class RayonCreateView(CreateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/create_rayon.html"

    def get_context_data(self, **kwargs):
        context = super(RayonCreateView, self).get_context_data(**kwargs)
        context['titremenu'] = "Ajout d'un nouveau rayon"
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('detailRayon', rayon.idRayon)


@method_decorator(login_required, name='dispatch')
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/update_rayon.html"

    def get_context_data(self, **kwargs):
        context = super(RayonUpdateView, self).get_context_data(**kwargs)
        context['titremenu'] = "Modification du rayon"
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('detailRayon', rayon.idRayon)


@method_decorator(login_required, name='dispatch')
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('ListeRayons')


@method_decorator(login_required, name='dispatch')
class StatutCreateView(CreateView):
    model = Statut
    form_class = StatutForm
    template_name = "monApp/create_statut.html"

    def get_context_data(self, **kwargs):
        context = super(StatutCreateView, self).get_context_data(**kwargs)
        context['titremenu'] = "Ajout d'un nouveau statut"
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        statut = form.save()
        return redirect('detailStatut', statut.idStatut)


@method_decorator(login_required, name='dispatch')
class StatutUpdateView(UpdateView):
    model = Statut
    form_class = StatutForm
    template_name = "monApp/update_statut.html"

    def get_context_data(self, **kwargs):
        context = super(StatutUpdateView, self).get_context_data(**kwargs)
        context['titremenu'] = "Modification du statut"
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        statut = form.save()
        return redirect('detailStatut', statut.idStatut)


@method_decorator(login_required, name='dispatch')
class StatutDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_statut.html"
    success_url = reverse_lazy('ListeStatuts')


@method_decorator(login_required, name='dispatch')
class ContenirCreateView(CreateView):
    model = Contenir
    form_class = ContenirForm
    template_name = "monApp/create_contenir.html"

    def get_context_data(self, **kwargs):
        context = super(ContenirCreateView, self).get_context_data(**kwargs)
        context['rayon'] = Rayon.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = Rayon.objects.get(pk=self.kwargs['pk'])
        produit = form.cleaned_data['produit']
        qte_saisie = form.cleaned_data['Qte']
        contenir_existant = Contenir.objects.filter(rayon=rayon, produit=produit).first()
        
        if contenir_existant:
            contenir_existant.Qte += qte_saisie
            contenir_existant.save()
        else:
            nouveau_contenir = Contenir(
                rayon=rayon,
                produit=produit,
                Qte=qte_saisie
            )
            nouveau_contenir.save()
            
        return redirect('detailRayon', rayon.idRayon)

class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'

    def post(self, request, **kwargs):
        identifiant= request.POST.get('username', False)
        motdepasse= request.POST.get('password', False)
        user = authenticate(username=identifiant, password=motdepasse)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/home.html', {'param': identifiant, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')


class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'

    def post(self, request, **kwargs):
        identifiant = request.POST.get('username', False)
        courriel = request.POST.get('mail', False)
        motdepasse = request.POST.get('password', False)
        user = User.objects.create_user(identifiant, courriel, motdepasse)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')


class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)