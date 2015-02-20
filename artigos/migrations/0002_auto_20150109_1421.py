# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artigo',
            options={'ordering': ('-publicacao',)},
        ),
        migrations.AlterField(
            model_name='artigo',
            name='publicacao',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data de Publicacao', blank=True),
            preserve_default=True,
        ),
    ]
