# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('artigos', '0002_auto_20150109_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(default=1, to='categorias.Categoria'),
            preserve_default=False,
        ),
    ]
