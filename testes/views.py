from django.http import HttpResponse
# from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.views import generic
from .models import Teste, Tag
from categorias.models import Categoria

from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# class DetailView(generic.DetailView):
#     model = Teste
#     template_name = 'testes/detail.html'

def detail(request, url_testeid):
    db_teste = get_object_or_404(Teste, pk=url_testeid)
    teste_tags = db_teste.tags.all()
    # teste = Teste.objects.get(id=url_testeid)
    categorias_list = Categoria.objects.all()
    return render(request, 'testes/detail.html', {
        'teste': db_teste,
        'teste_tag': teste_tags,
        'categorias_list': Categoria.objects.all(),
        })

def testes_index(request):

    testes_list = Teste.objects.all()
    tag = request.GET.get('tag','').split(',')
    # tag2 = request.GET.get('tag2',)
    categoria = request.GET.get('categoria',0)
    categoria_nome = 0
    tag_nome = None
    # tag = None
    
    if categoria > 0:
        testes_list = testes_list.filter(categoria=categoria)
        categoria_nome = Categoria.objects.get(pk=categoria)


    if tag:
        testes_list = testes_list.filter(tags__in=tag).distinct()
        tag_nome = Tag.objects.filter(id__in=tag).distinct()

    return render(request, 'testes/index.html', {
        'testes_list': testes_list,
        'categorias_list': Categoria.objects.all(),
        'categoria_nome':  categoria_nome,
        'tag_nome': tag_nome,
        # 'tag_nome2': tag_nome2,
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