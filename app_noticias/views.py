from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import ListView, FormView, TemplateView
from .models import Noticia, Tag, MensagemDeContato
from django.urls import reverse
from .forms import ContatoForm
# Create your views here.
'''
class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'
'''
def home(request):
    noticias = Noticia.objects.order_by('data_publicacao').reverse()
    return render(request, 'app_noticias/home.html', {'noticias':noticias})

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


def slug_view(request, pk):
    try:
        noticia = Noticia.objects.filter(tags__slug=pk).order_by('data_publicacao').reverse()
    
    except Noticia.DoesNotExist:
        raise Http404('Notícias não encontradas.')

    return render(request, 'app_noticias/tag.html', {'noticia': noticia})

class ContatoView(FormView):
    template_name = 'app_noticias/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')

class ContatoSucessoView(TemplateView):
    template_name = 'app_noticias/contato_sucesso.html'