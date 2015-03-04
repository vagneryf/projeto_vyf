from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.testes_index, name='testes_index'),
    # url(r'^lista/', views.listing, name='listing'),
    # url(r'^(?P&lt;pk&gt;\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<url_testeid>\d+)/$', views.detail, name='detail'),
)