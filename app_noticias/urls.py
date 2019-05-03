from django.urls import path
from app_noticias.views import * #noticias_resumo, HomePageView, noticias_resumo_template
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('noticias/resumo/', noticias_resumo_template, name = 'resumo'),
    path('noticias/<int:noticia_id>/', noticia_detalhes, name = 'detalhes'),
    path('<str:pk>', lista_tag, name='tag'),
]