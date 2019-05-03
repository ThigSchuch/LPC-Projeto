from django.contrib import admin
from .models import Noticia, Pessoa, Tag

# Register your models here.

@admin.register(Noticia,Tag,Pessoa)

class NoticiaAdmin(admin.ModelAdmin):
    pass