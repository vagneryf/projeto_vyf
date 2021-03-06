from django.contrib import admin
from artigos.models import Artigo
from categorias.models import Categoria
# from easy_select2 import select2_modelform

# Register your models here.

# TestForm = select2_modelform(Artigo, attrs={'width': '250px'})

class ArtigoAdmin(admin.ModelAdmin):
	list_display = ('titulo','publicacao','categoria',)
	fieldsets = [
		(None, {'fields': ['titulo']}),
    	('Data publicacao', {'fields': ['publicacao']}),
    	('Texto', {'fields': ['conteudo']}),
    	('Categoria',{'fields':['categoria']})

	]
	list_filter = ['publicacao','categoria']
	search_fields = ['titulo']
	# form = TestForm

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/tinymce_setup.js',
		]

admin.site.register(Artigo, ArtigoAdmin)

