# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from datetime import datetime, timedelta
from categorias.models import Categoria
from artigos.models import Artigo
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'tags'

    def __unicode__(self):
        return self.name

def limit_publicacao_choices():
    return {'publicacao__lte': datetime.now()}

# def filtros_q():
#     # data_hoje = datetime.now()
#     # data_antes = data_hoje - timedelta(days=190)
#     # testes_in = Teste.objects.all()[:3]
#     # filtro_q = Q(id__in=testes_in) & Q(publicacao__range=(data_antes, data_hoje)) & Q(categoria=6)
#     testes_in = Teste.objects.filter(categoria='6').filter(publicacao__lte=datetime.now()).values_list('id', flat=True)[:3]
#     m = [8]
#     # testes_ex = Teste.objects.filter(id__in=m).values_list('id', flat=True)
#     # n = 'self.relacao_teste'
#     # testes_ex = Teste.objects.filter(id__in=n).values_list('id', flat=True)
#     # testes_ex = list(testes_ex)
#     testes_in = list(testes_in)
#     # testes_in.extend(m)
#     testes_in += m
#     filtro_q = Q(id__in=testes_in)
#     return filtro_q
    
class Teste(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField('Data de Publicacao', default=datetime.now, blank=True)
    # colocar o default=datetime.now, blank=True para data atual automatica
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)  # To demonstrate select2 multiple
    # tags_2 = models.CharField(Tag, max_length=100, blank=True, null=True)
    # teste_art = models.ManyToManyField(Artigo, blank=True, null=True)

    relacao_teste = models.ManyToManyField('self', blank=True, null=True, symmetrical=False)#, limit_choices_to=filtros_q, help_text=u'Selecione 2 artigos no máximo. ')
    


    # try:
    #     relacao_existente_id = self.relacao_teste.all().values_list('id', flat=True)
    #     print 'veio'
    # except Exception, e:
    #     pass
    # def clean_relacao_teste(self):
    #     relacao_verificar = self.relacao_teste
    #     if len(relacao_verificar) > 2:
            # self.relacao_teste = None
            # return self.relacao_teste
            # raise ValidationError(u'Adicionar no máximo 2 artigos!!')
        # else:
        #     return relacao_verificar

    def __unicode__(self):
        return self.titulo #, self.conteudo, self.publicacao
        # erro ao retornar + de um item em self
    class Meta:
        ordering = ('-publicacao',) # ordena a ordem dos artigos
