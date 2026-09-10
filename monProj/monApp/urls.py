from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="default"),
    path('home/<param>',views.home ,name='home'),
    path("contact/", views.contact, name="contact"),
    path("aboutus/", views.aboutus, name="aboutus")
]