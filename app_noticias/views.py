from django.shortcuts import render
from django.views.generic import ListView
from .models import Noticia
# Create your views here.

class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'