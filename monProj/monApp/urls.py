from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path("", views.home, name="home"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<param>", views.HomeView.as_view(), name="home"),
    #path("contact/", views.ContactView.as_view(), name="contact"),
    path("contact/",views.ContactView.as_view() , name="contact"),
    path("email-sent/", views.EmailSentView, name="email-sent"),
    path("about/", views.AboutView.as_view(), name="about"),
    #path("home/", views.home, name="home"),
    #path('', views.home, name="default"),
    #path('home/', views.home, name="default"),
    #path('home/<param>',views.home ,name='home'),
    #path("contact/", views.contact, name="contact"),
    #path("aboutus/", views.aboutus, name="aboutus"),
    path('produits/',views.ProduitListView.as_view(),name='listProduits'),
    path("produit/<int:pk>/",views.ProduitDetailView.as_view(), name='detailProduit'),
    #path('produits/',views.ListProduits ,name='produits'),
    path("produit/",views.ProduitCreateView.as_view(), name="creationProduit"),
    path("produit/<pk>/update/",views.ProduitUpdateView.as_view(), name="modificationProduit"),
    path("produit/<pk>/delete/",views.ProduitDeleteView.as_view(), name="suppressionProduit"),

    path("categories/", views.CategorieListView.as_view(), name="ListeCategories"),
    path("categorie/<int:pk>/",views.CategorieDetailView.as_view(), name='detailCategorie'),
    path("categorie/", views.CategorieCreateView.as_view(), name="creationCategorie"),
    path("categorie/<pk>/update/", views.CategorieUpdateView.as_view(), name="modificationCategorie"),
    path("categorie/<pk>/delete/", views.CategorieDeleteView.as_view(), name="suppressionCategorie"),
    # path("ListeCategories/", views.ListeCategories, name="ListeCategories"),

    path("rayons/", views.RayonListView.as_view(), name="ListeRayons"),
    path("rayon/<int:pk>/",views.RayonDetailView.as_view(), name='detailRayon'),
    path("rayon/", views.RayonCreateView.as_view(), name="creationRayon"),
    path("rayon/<pk>/update/", views.RayonUpdateView.as_view(), name="modificationRayon"),
    path("rayon/<pk>/delete/", views.RayonDeleteView.as_view(), name="suppressionRayon"),
    #path("ListeRayons/", views.ListeRayons, name="ListeRayons"),

    path("statuts/", views.StatutListView.as_view(), name="ListeStatuts"),
    path("statut/<int:pk>/",views.StatutDetailView.as_view(), name='detailStatut'),
    path("statut/", views.StatutCreateView.as_view(), name="creationStatut"),
    path("statut/<pk>/update/", views.StatutUpdateView.as_view(), name="modificationStatut"),
    path("statut/<pk>/delete/", views.StatutDeleteView.as_view(), name="suppressionStatut"),
    # path("ListeStatuts/", views.ListeStatuts, name="ListeStatuts")
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
    

]
