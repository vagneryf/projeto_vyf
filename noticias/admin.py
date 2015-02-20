from django.contrib import admin
from noticias.models import Noticia
# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo','publicacao')
	fieldsets = [
		(None, {'fields': ['titulo']}),
    	('Data publicacao', {'fields': ['publicacao']}),
    	('Texto', {'fields': ['conteudo']})
	]
	list_filter = ['publicacao']
	search_fields = ['titulo']

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/tinymce_setup.js',
		]

admin.site.register(Noticia, NoticiaAdmin)