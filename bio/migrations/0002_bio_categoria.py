# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='categoria',
            field=models.ForeignKey(blank=True, to='categorias.Categoria', null=True),
            preserve_default=True,
        ),
    ]
