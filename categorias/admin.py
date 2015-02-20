from django.contrib import admin
from categorias.models import Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nome','detalhe')
	fieldsets = [
		('Categoria', {'fields': ['nome']}),
		('Detalhes', {'fields': ['detalhe']})
	]
	search_fields = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
