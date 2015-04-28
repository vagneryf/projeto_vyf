# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0008_teste_mood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teste',
            name='mood',
        ),
        migrations.AddField(
            model_name='teste',
            name='relacao_teste',
            field=models.ManyToManyField(related_name='relacao_teste_rel_+', null=True, to='testes.Teste', blank=True),
            preserve_default=True,
        ),
    ]
