# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0011_auto_20150428_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='relacao_teste',
            field=models.ManyToManyField(related_name='+', null=True, to='testes.Teste', blank=True),
            preserve_default=True,
        ),
    ]
