from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Categoria

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'categorias/index.html'
	context_object_name = 'categoria_list'

	def get_queryset(self):
		return Categoria.objects.all().order_by('nome')[:20]
