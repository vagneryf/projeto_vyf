# -*- coding: utf-8 -*-
from django.db import models

class Grupo(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(u'E-mail', null=False, blank=False)

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    def __unicode__(self):
        return self.nome

class Integrante(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(u'E-mail', null=False, blank=False)

    class Meta:
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"

    def __str__(self):
        pass

