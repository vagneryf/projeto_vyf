from django.http import HttpResponse
# from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.views import generic
from .models import Teste
from categorias.models import Categoria

from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class DetailView(generic.DetailView):
    model = Teste
    template_name = 'testes/detail.html'

def testes_index(request):

    testes_list = Teste.objects.all()
    categoria = request.GET.get('categoria',0)
    categoria_nome = 0
    
    if categoria > 0:
        testes_list = testes_list.filter(categoria=categoria)
        categoria_nome = Categoria.objects.get(pk=categoria)

    return render(request, 'testes/index.html', {
        'testes_list': testes_list,
        'categorias_list': Categoria.objects.all(),
        'categoria_nome':  categoria_nome,
        })

# def listing(request):
#     testes_list = Teste.objects.all()
#     paginator = Paginator(testes_list, 5)

#     page = request.GET.get('page')
#     try:
#         testes = paginator.page(page)
#     except PageNotAnInteger:
#         testes = paginator.page(1)
#     except EmptyPage:
#         testes = paginator.page(paginator.num_page)

#     return render_to_response('testes/list.html', {"testes": testes})