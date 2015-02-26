# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('publicacao', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Data de Publicacao', blank=True)),
                ('categoria', models.ForeignKey(blank=True, to='categorias.Categoria', null=True)),
            ],
            options={
                'ordering': ('-publicacao',),
            },
            bases=(models.Model,),
        ),
    ]
