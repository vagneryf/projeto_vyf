from django.db import models
from datetime import datetime

# Create your models here.
class Noticia(models.Model):
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	publicacao = models.DateTimeField('Data de Publicacao', default=datetime.now, blank=True)
	def __unicode__(self):
		return self.titulo #, self.conteudo, self.publicacao
		# erro ao retornar + de um item em self