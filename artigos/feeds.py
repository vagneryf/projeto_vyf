# para RSS de artigos
from django.contrib.syndication.views import Feed
from models import Artigo

class UltimosArtigos(Feed):
	title = 'Ultimo artigos do site Projeto VYF'
	link = '/'

	def items(self):
		return Artigo.objects.all()

	def item_link(self, artigo):
		return '/artigo/%d/'%artigo.id