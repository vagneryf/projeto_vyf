from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.testes_index, name='testes_index'),
	# url(r'^lista/', views.listing, name='listing'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)