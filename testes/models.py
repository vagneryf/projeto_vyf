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

def limit_publicacao_choices():
    return {'publicacao__lte': datetime.now()}

# def limit_quant_choices():
#     return ()

class Teste(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField('Data de Publicacao', default=datetime.now, blank=True)
    # colocar o default=datetime.now, blank=True para data atual automatica
    categoria = models.ForeignKey(Categoria, null=True, blank=True)

    # tag = models.CharField(blank=False, default='', max_length=64,
 #                            help_text='Insira a tag')
    tags = models.ManyToManyField(Tag, blank=True, null=True)  # To demonstrate select2 multiple
    tags_2 = models.CharField(Tag, max_length=100, blank=True, null=True)
    teste_art = models.ManyToManyField(Artigo, blank=True, null=True)

    # mood = models.CharField(blank=False, default='', max_length=64,
    #                         help_text='What is your current mood?')

    relacao_teste = models.ManyToManyField("self", blank=True, null=True, symmetrical=False, limit_choices_to = limit_publicacao_choices)# related_name='+') limit_choices_to={'id': 1}, ) # through='RelacaoTeste', symmetrical=False, related_name='related_to')

    def __unicode__(self):
        return self.titulo #, self.conteudo, self.publicacao
        # erro ao retornar + de um item em self
    class Meta:
        ordering = ('-publicacao',) # ordena a ordem dos artigos


# class RelacaoTeste(models.Model):
#     from_teste = models.ForeignKey(Teste, related_name='from_teste')
#     to_teste = models.ForeignKey(Teste, related_name='to_teste')