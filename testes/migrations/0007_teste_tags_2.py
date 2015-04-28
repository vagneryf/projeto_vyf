# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import testes.models


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0006_teste_teste_art'),
    ]

    operations = [
        migrations.AddField(
            model_name='teste',
            name='tags_2',
            field=models.CharField(default=0, max_length=100, verbose_name=testes.models.Tag),
            preserve_default=False,
        ),
    ]
