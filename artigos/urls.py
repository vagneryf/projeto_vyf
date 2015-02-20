from django.conf.urls import patterns, url
from . import views
# from artigos import views
from artigos.feeds import UltimosArtigos

urlpatterns = patterns('',
	# pagina simples de teste
	# url(r'^$', views.index, name='index'), 

	# pagina de listagem dos artigos que recebe parametros categoria=2:
	url(r'^$', views.artigos_index, name='artigos_index'),
	url(r'^lista/', views.listing, name='listing'),
	# Generic view com a classe IndeView:
	# url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^noticias/', views.ListaNoticia.as_view(), name='noticias'),
	# url(r'^categoria/', views.CategoriaListView.as_view(), name='categoria'),
	

	# url(r'^(?P<url_artigoid>\d+)\.html$', views.artigo_read, name='artigo_read'),

	# adicionar o RSS de artigos:
    # (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.Feed',
    #     {'feed_dict': {'ultimos': UltimosArtigos}}),
)
