# -*- coding: utf-8 -*-
import datetime
from django.db import models
# from datetime import datetime
from datetime import timedelta
from django.utils import timezone
# Create your models here.
from django.core.exceptions import ValidationError

# def validate_data_inicio(value):
#     if value < self.data_inicio:
#         raise ValidationError(u'data errada')

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    data_inicio = models.DateTimeField(u'Data início', default=timezone.now, blank=True)
    # data_inicio = models.DateTimeField(u'Data início', default=datetime.now, blank=True)
    # data_fim = models.DateTimeField(u'Data fim', default=lambda: timezone.now()+timedelta(minutes=15), blank=True)
    
    def mais_quinze():
        return timezone.now()+timedelta(minutes=15)

    data_fim = models.DateTimeField(u'Data fim (mín = 15min)', default=mais_quinze, blank=True)
    # Verificar depois como fica a categoria ou tag
    categoria = models.CharField(max_length=100, null=True)
    texto_simples = models.CharField(max_length=300, null=True)
    texto_maior = models.TextField()
    # Ver o esquema de maps
    local = models.CharField(max_length=300, null=False)
    tag = models.CharField(max_length=150, null=True)
    sub_evento = models.ForeignKey("self", null=True, blank=True)

    def mais_quinze():
        return datetime.now() + timedelta(days = 30)

    def __unicode__(self):
        return self.titulo

    def evento_em_andamento(self):
        agora = timezone.now()
        # agora - datetime.timedelta(days=1)
        return self.data_inicio <= agora <= self.data_fim
    evento_em_andamento.admin_order_field = 'data_inicio'
    evento_em_andamento.boolean = True
    evento_em_andamento.short_description = 'Em andamento?'  

    class Meta:
        ordering = ('-data_inicio',)

    # def erro_data(self):
    #     if self.data_inicio > self.data_fim:
    #         raise ValidationError(u'data errada')
    
    def clean(self):
        conf_data_inicio = self.data_inicio+timedelta(minutes=15)
        if conf_data_inicio > self.data_fim:
            raise ValidationError(u'Erro data início deve ser menor que a data fim, ou fim deve ser maior que início. Duração mínima: 15 minutos!!')
        # if self.data_fim < self.data_inicio:
        #     raise ValidationError('Erro data fim deve ser maior que a data fim.')
        if self.sub_evento is not None:
            if self.data_inicio < self.sub_evento.data_inicio:
                raise ValidationError(u'Erro data inicio sub evento deve ser maior que data inicio evento pai.')
            if self.data_fim > self.sub_evento.data_fim:
                raise ValidationError(u'Erro data fim sub evento deve ser menor que data fim evento pai')

    # def save(self, *args, **kwargs):
    #     if self.sub_evento is not None:
    #         self.data_inicio = max(self.sub_evento.data_inicio, self.data_inicio)
    #         self.data_fim = min(self.sub_evento.data_fim, self.data_fim)
    #         # raise ValidationError("teste")
    #     # if self.data_inicio > self.data_fim:
    #     #     return
    #     super(Evento, self).save(*args, **kwargs)
