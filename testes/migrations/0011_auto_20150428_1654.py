# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0010_auto_20150428_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='teste_art',
            field=models.ManyToManyField(to='artigos.Artigo', null=True, blank=True),
            preserve_default=True,
        ),
    ]
