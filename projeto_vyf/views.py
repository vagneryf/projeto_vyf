# from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.shortcuts import render
from artigos.models import Artigo
from categorias.models import Categoria
from django.utils import timezone
from eventos.models import Evento


# pagina simples da home apenas com o texto para teste
# def home(request):
#  	return HttpResponse('index.html')

def home(request):
	return render(request,'index.html',{
		'artigos_list': Artigo.objects.all().order_by('-publicacao')[:5],
		'noticias_list': Artigo.objects.filter(categoria='6').order_by('-publicacao')[:5],
		'categorias_list': Categoria.objects.all(),
		'eventos_list' : Evento.objects.filter(data_inicio__range=(timezone.now(),timezone.now()+datetime.timedelta(days=30))).order_by('data_inicio')[:3],
		})

# pagina home baseada no index + base

# class IndexView(generic.ListView):
# 	template_name = 'artigos/artigos_lista.html'
# 	context_object_name = 'artigos_list'

# 	def get_queryset(self):
# 	 	return Artigo.objects.all().order_by('-publicacao')[:5]
