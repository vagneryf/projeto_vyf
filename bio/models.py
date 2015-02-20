from django.db import models
from datetime import datetime
# Create your models here.
from categorias.models import Categoria

class Bio(models.Model):
	nome = models.CharField(max_length=100)
	informacoes = models.TextField()
	publicacao = models.DateTimeField('Data de Publicacao', default=datetime.now, blank=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True)

	def __unicode__(self):
		return self.nome
	class Meta:
		ordering = ('nome',)
