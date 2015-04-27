# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0004_auto_20150122_1518'),
        ('testes', '0005_auto_20150226_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='teste_art',
            field=models.ManyToManyField(to='artigos.Artigo'),
            preserve_default=True,
        ),
    ]
