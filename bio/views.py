from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Bio
from categorias.models import Categoria
# Create your views here.

#  pode receber parametro categoria=2:
def bios_index (request):
	bios_list = Bio.objects.all()
	categoria = request.GET.get('categoria', 0)
	categoria_nome = 0
	if categoria > 0:
		bios_list = bios_list.filter(categoria=categoria)
		categoria_name = Categoria.objects.get(pk=categoria)
	return render(request, 'bio/index.html',{
		'bio_list' : bios_list,
		'categorias_list' : Categoria.objects.all(),
		'categoria_nome' : categoria_nome,
		})

# class IndexView(generic.ListView):
# 	template_name = 'bio/index.html'
# 	context_object_name = 'bio_list'

# 	def get_queryset(self):
# 		return Bio.objects.all().order_by('nome')[:20]

class DetailView(generic.DetailView):
	model = Bio
	template_name = 'bio/detail.html'
