from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'telefone', 'email', 'categoria']
    list_display_links = ['id', 'nome', 'telefone']
    search_fields = ['nome', 'sobrenome', 'telefone', 'email']


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
