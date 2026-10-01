from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="default"),
    path('home/', views.home, name="default"),
    path('home/<param>',views.home ,name='home'),
    path("contact/", views.contact, name="contact"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path('produits/',views.ListProduits ,name='produits'),
    path("ListeCategories/", views.ListeCategories, name="ListeCategories"),
    path("ListeRayons/", views.ListeRayons, name="ListeRayons"),
    path("ListeStatuts/", views.ListeStatuts, name="ListeStatuts")
]

