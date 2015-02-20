# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('publicacao', models.DateTimeField(verbose_name=b'Data de Publicacao')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
