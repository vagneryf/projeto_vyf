from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Noticia

# pagina simples de teste do view
# def index(request):
# 	return HttpResponse("Teste da pagina de artigo sem nada")

class IndexView(generic.ListView):
	template_name = 'noticias/index.html'
	context_object_name = 'noticias_list'

	def get_queryset(self):
	 	return Noticia.objects.all().order_by('-publicacao')[:10]

class DetailView(generic.DetailView):
	model = Noticia
	template_name = 'noticias/detail.html'