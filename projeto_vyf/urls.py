from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from filebrowser.sites import site
from artigos import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')), # para incluir grappelli
    # pagina simples baseada em request de home
    url(r'^$', 'projeto_vyf.views.home', name='home'),
    # generic view com a classe IndexView:
    # url(r'^$', views.IndexView.as_view(), name='index'),
    #  pagina usando generic views
    # url(r'^$', TemplateView.as_view(template_name="projeto_vyf/index.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artigos/', include('artigos.urls', namespace="artigos")),
    # url(r'^artigos/lista', include('artigos.urls', namespace="artigos_lista")),
    # url(r'^noticias/', include('noticias.urls', namespace="noticias")),
    # url(r'^rss/', include('artigos.urls', namespace="rss")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^categorias/', include('categorias.urls', namespace="categorias")),
    url(r'^bio/', include('bio.urls', namespace="bio")),
    url(r'^eventos/', include('eventos.urls', namespace="eventos")),
    (r'^comments/', include('django.contrib.comments.urls')),
    # url(r'^categoria/', include('artigos.urls', namespace="index_cat")),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^select2/', include('django_select2.urls')), # para usar o select2
)
