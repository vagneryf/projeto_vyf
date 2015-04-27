# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from categorias.models import Categoria
from artigos.models import Artigo


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'tags'

    def __unicode__(self):
        return self.name



class Teste(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField('Data de Publicacao', default=datetime.now, blank=True)
    # colocar o default=datetime.now, blank=True para data atual automatica
    categoria = models.ForeignKey(Categoria, null=True, blank=True)

    # tag = models.CharField(blank=False, default='', max_length=64,
 #                            help_text='Insira a tag')
    tags = models.ManyToManyField(Tag)  # To demonstrate select2 multiple

    teste_art = models.ManyToManyField(Artigo)

    def __unicode__(self):
        return self.titulo #, self.conteudo, self.publicacao
        # erro ao retornar + de um item em self
    class Meta:
        ordering = ('-publicacao',) # ordena a ordem dos artigos