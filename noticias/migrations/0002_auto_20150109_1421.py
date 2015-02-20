# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='publicacao',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data de Publicacao', blank=True),
            preserve_default=True,
        ),
    ]
