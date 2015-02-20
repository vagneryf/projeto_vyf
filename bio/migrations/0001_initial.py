# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('informacoes', models.TextField()),
                ('publicacao', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data de Publicacao', blank=True)),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
    ]
