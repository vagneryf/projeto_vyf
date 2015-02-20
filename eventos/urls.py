from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.eventos_index, name='eventos_index'),
	# generic IndexView:
	# url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)