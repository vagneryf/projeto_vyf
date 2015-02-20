# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('data_inicio', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data in\xedcio', blank=True)),
                ('data_fim', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data fim', blank=True)),
                ('categoria', models.CharField(max_length=100, null=True)),
                ('texto_simples', models.CharField(max_length=300, null=True)),
                ('texto_maior', models.TextField()),
                ('local', models.CharField(max_length=300, null=True)),
                ('tag', models.CharField(max_length=150, null=True)),
            ],
            options={
                'ordering': ('-data_inicio',),
            },
            bases=(models.Model,),
        ),
    ]
