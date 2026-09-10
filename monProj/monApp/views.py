from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def contact(request):
    return HttpResponse("<h1>Bienvenue sur la page de contact</h1>")

def aboutus(request):
    return HttpResponse("<h1>Bienvenue sur la page d'infomations</h1>")