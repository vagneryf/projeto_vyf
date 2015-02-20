# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0003_artigo_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(blank=True, to='categorias.Categoria', null=True),
            preserve_default=True,
        ),
    ]
