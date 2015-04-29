# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import Teste, Tag
from categorias.models import Categoria
from easy_select2 import select2_modelform, select2_modelform_meta, Select2TextInput


class TesteAdmin(admin.ModelAdmin):
    list_display = ('titulo','publicacao','categoria',)
    # fieldsets = [
    #     (None, {'fields': ['titulo']}),
    #     ('Data publicacao', {'fields': ['publicacao']}),
    #     ('Texto', {'fields': ['conteudo']}),
    #     ('Categoria',{'fields':['categoria']})
    #     ('Testes', {'fields':['tags', 'tags2', 'teste_art', 'relacao_teste']})
    #     ]
    list_filter = ['publicacao','categoria']
    search_fields = ['titulo']

    class Media:
      js = [
          '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
          '/static/tinymce_setup.js',
      ]


# TesteForm = select2_modelform(Teste, attrs={'width': '350px'})

# class TesteForm(forms.ModelForm):
#     Meta = select2_modelform(Teste, attrs={'width': '350px'})

# class TesteAdmin(admin.ModelAdmin):
#     form = TesteForm
#     list_display = ('id','titulo','publicacao','categoria')
#     list_filter = ['publicacao','categoria']
#     search_fields = ['titulo']

#     class Media:
#         js = [
#             '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
#             '/static/tinymce_setup.js',
#         ]



admin.site.register(Tag)
admin.site.register(Teste, TesteAdmin)