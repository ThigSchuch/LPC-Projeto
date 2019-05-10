from django.contrib import admin
from .models import Noticia, Pessoa, Tag, MensagemDeContato

# Register your models here.

@admin.register(Noticia,Tag,Pessoa,MensagemDeContato)

class NoticiaAdmin(admin.ModelAdmin):
    pass

class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)