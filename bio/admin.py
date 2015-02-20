from django.contrib import admin
from bio.models import Bio
from categorias.models import Categoria
# Register your models here.

class BioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'publicacao','categoria',)
	fieldsets = [
		('Nome', {'fields': ['nome']}),
		('Data de Publicacao', {'fields': ['publicacao']}),
		('Informacoes', {'fields': ['informacoes']}),
		('Categoria', {'fields':['categoria']})
	]
	list_filter = ['publicacao','categoria']
	search_fields = ['nome']

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/tinymce_setup.js',
		]	

admin.site.register(Bio, BioAdmin)
