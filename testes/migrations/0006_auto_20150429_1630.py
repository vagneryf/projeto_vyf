# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0005_auto_20150226_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='relacao_teste',
            field=models.ManyToManyField(help_text='Selecione 2 artigos no m\xe1ximo. ', to='testes.Teste', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teste',
            name='tags',
            field=models.ManyToManyField(to='testes.Tag', null=True, blank=True),
            preserve_default=True,
        ),
    ]
