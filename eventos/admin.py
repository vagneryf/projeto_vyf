# -*- coding: utf-8 -*-
from django.contrib import admin
from eventos.models import Evento
# from categorias.models import Categoria

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
	list_display = ('titulo','data_inicio','data_fim','categoria', 'evento_em_andamento',)
	fieldsets = [
		# (u'Título', {'fields': ['titulo']}),
		# (None, {'fields': ['data_inicio']}),
		# (None, {'fields': ['data_fim'],}),
		# (None, {'fields': ['categoria']}),
		# (None, {'fields': ['texto_simples']}),
		# (None, {'fields': ['texto_maior']}),
		# (None, {'fields': ['local']}),
		# (None, {'fields':['tag']}),
	]
	list_filter = ['data_inicio','data_fim','categoria']
	search_fields = ['titulo']

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/tinymce_setup.js',
		]

admin.site.register(Evento, EventoAdmin)