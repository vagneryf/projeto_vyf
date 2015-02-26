# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from categorias.models import Categoria

class Teste(models.Model):
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	publicacao = models.DateTimeField('Data de Publicacao', default=datetime.now, blank=True)
	# colocar o default=datetime.now, blank=True para data atual automatica
	categoria = models.ForeignKey(Categoria, null=True, blank=True)
	def __unicode__(self):
		return self.titulo #, self.conteudo, self.publicacao
		# erro ao retornar + de um item em self
	class Meta:
		ordering = ('-publicacao',) # ordena a ordem dos artigos