from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path("", views.home, name="home"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<param>", views.HomeView.as_view(), name="home"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    #path("home/", views.home, name="home"),
    #path('', views.home, name="default"),
    #path('home/', views.home, name="default"),
    #path('home/<param>',views.home ,name='home'),
    #path("contact/", views.contact, name="contact"),
    #path("aboutus/", views.aboutus, name="aboutus"),
    path('produits/',views.ProduitListView.as_view(),name='produits'),
    path("produit/<int:pk>/",views.ProduitDetailView.as_view(), name='detailProduit'),
    #path('produits/',views.ListProduits ,name='produits'),
    path("ListeCategories/", views.ListeCategories, name="ListeCategories"),
    path("ListeRayons/", views.ListeRayons, name="ListeRayons"),
    path("ListeStatuts/", views.ListeStatuts, name="ListeStatuts")
]

