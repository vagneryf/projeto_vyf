from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',

	# exibicao de pagina simples anterior sem class
	# # ex: /polls/
	# url(r'^$', views.index, name='index'),
	# # ex: /polls/5/
	# url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	# # ex: polls/5/results/
	# url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
	# # ex: /polls/5/vote/
	# url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

	# exibicao de pagina com class formato padrao do django ver em views.py
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
