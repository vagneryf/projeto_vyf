from django.db import models

# Create your models here.
class Categoria(models.Model):
	nome = models.CharField(max_length=100)
	detalhe = models.TextField()
	def __unicode__(self):
		return self.nome
	class Meta:
		ordering = ('nome',)