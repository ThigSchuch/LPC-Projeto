from django.db import models

# Create your models here.
class Noticia(models.Model):

    class Meta:
        verbose_name = 'Notícias'
        verbose_name_plural = 'Notícias'

    titulo = models.CharField('Título', max_length=128)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField()
    data_publicacao = models.DateTimeField()
    publicado = models.BooleanField()