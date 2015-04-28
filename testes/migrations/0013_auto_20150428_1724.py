# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0012_auto_20150428_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='relacao_teste',
            field=models.ManyToManyField(to='testes.Teste', null=True, blank=True),
            preserve_default=True,
        ),
    ]
