# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import Teste, Tag
from categorias.models import Categoria
# from django.db.models import Q
from datetime import datetime, timedelta
# from easy_select2 import select2_modelform, select2_modelform_meta, Select2TextInput

# class TesteAdmin(admin.ModelAdmin):
#     list_display = ('titulo','publicacao','categoria',)
#     # fieldsets = [
#     #     (None, {'fields': ['titulo']}),
#     #     ('Data publicacao', {'fields': ['publicacao']}),
#     #     ('Texto', {'fields': ['conteudo']}),
#     #     ('Categoria',{'fields':['categoria']})
#     #     ('Testes', {'fields':['tags', 'tags2', 'teste_art', 'relacao_teste']})
#     #     ]
#     list_filter = ['publicacao','categoria']
#     search_fields = ['titulo']

#     class Media:
#       js = [
#           '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
#           '/static/tinymce_setup.js',
#       ]


class TesteAdminForm(forms.ModelForm):
    class Meta:
        model = Teste
        exclude = ['publicacao']

    def __init__(self, *args, **kwargs):
        super(TesteAdminForm, self).__init__(*args, **kwargs)
        s = []
        print self.instance.id, type(self.instance)
        if self.instance.id:
            ts = self.instance.relacao_teste
            s = ts.all().values_list('id', flat=True)
            s = list(s)
        t = Teste.objects.filter(categoria='6').filter(publicacao__lte=datetime.now()).values_list('id', flat=True)[:3]
        t = list(t)
        t += s
        qs = Teste.objects.filter(id__in=t)
        # if self.instace.id:
        #     qs = qs.exclude(id=self.instance.id)
        self.fields['relacao_teste'].queryset = qs


class TesteAdmin(admin.ModelAdmin):
    form = TesteAdminForm
    list_display = ('titulo','publicacao','categoria',)
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