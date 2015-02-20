# from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.views import generic
from .models import Artigo
from categorias.models import Categoria

from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# pagina simples de teste do view
# def index(request):
#   return HttpResponse("Teste da pagina de artigo sem nada")

# generic ListView padrao com classe:
# class IndexView(generic.ListView):
#     template_name = 'artigos/index.html'
#     context_object_name = 'artigos_list'

#     def get_queryset(self):
#         return Artigo.objects.all().order_by('-publicacao')[:10]

class DetailView(generic.DetailView):
    model = Artigo
    template_name = 'artigos/detail.html'

# generic ListView listagem com filtro
class ListaNoticia(generic.ListView):
    template_name = 'artigos/index.html'
    context_object_name = 'artigos_list'

    def get_queryset(self):
        return Artigo.objects.filter(categoria=6).order_by('-publicacao')[:10]

# class CategoriaListView(generic.ListView):
#   template_name = 'artigos/index.html'
#   context_object_name = 'artigos_list'

#   def get_queryset(self):
#       return Artigo.objects.filter(categoria=2).order_by('-publicacao')[:10]

# def artigo_read(request, url_artigoid):
#   db_artigo = get_object_or_404(Artigo, pk=url_artigoid)
#   Artigo.objects.filter(pk=url_artigoid)

#   return render(request, 'detail.html', {
#       'db_artigo': db_artigo,
#       })

# list view com parametro na url ex: categoria=2

def artigos_index(request):

    artigos_list = Artigo.objects.all()
    categoria = request.GET.get('categoria',0)
    categoria_nome = 0
    
    if categoria > 0:
        artigos_list = artigos_list.filter(categoria=categoria)
        categoria_nome = Categoria.objects.get(pk=categoria)

    return render(request, 'artigos/index.html', {
        'artigos_list': artigos_list,
        'categorias_list': Categoria.objects.all(),
        'categoria_nome':  categoria_nome,
        })

    # categoria = request.Get.get('categoria')
    # # if secao not in ('', None, 0):
    # #     try:
    # #         secao = int(secao)
    # #     except Exception:
    # #         raise Http404(u"Seco precisa ser numerica")
    # # else:
    # artigos_list = artigos_list.filter(categoria=categoria)
    #   # try:
    #   #   h1_append = Secao.objects.get(pk=secao)
    #   # except ObjectDoesNotExist:
    #   #   h1_append = u'(Secao inesistente)'
    # return HttpResponse("Teste da pagina de artigo sem nada")

def listing(request):
    artigos_list = Artigo.objects.all()
    paginator = Paginator(artigos_list, 5)

    page = request.GET.get('page')
    try:
        artigos = paginator.page(page)
    except PageNotAnInteger:
        artigos = paginator.page(1)
    except EmptyPage:
        artigos = paginator.page(paginator.num_page)

    return render_to_response('artigos/list.html', {"artigos": artigos})