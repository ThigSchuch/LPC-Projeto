from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import ListView
from .models import Noticia, Tag
# Create your views here.

class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'

def noticias_resumo_template(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total':total})
'''
def noticias_resumo(request):
    total = Noticia.objects.count()
    html = """
    <html>
    <body>
    <h1>Resumim</h1>
    <p>Suas notícias somam um total de {}, oxente.</p>
    </body>
    </html>
    """.format(total)
    return HttpResponse(html)
'''
def noticia_detalhes(request, noticia_id):
    try:
        noticia = Noticia.objects.get(pk = noticia_id)

    except Noticia.DoesNotExist:
        raise Http404('Notícia não encontrada')

    return render(request, 'app_noticias/detalhes.html', {'noticia':noticia})

def lista_tag(request, pk):
    try:
        noticia = Noticia.objects.all()
        tag = pk

    except Noticia.DoesNotExist:
        raise Http404('Notícias não encontradas.')

    return render(request, 'app_noticias/tag.html', {'noticias': noticia,'tag':tag})