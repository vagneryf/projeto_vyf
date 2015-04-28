# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import testes.models


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0009_auto_20150428_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teste',
            name='tags',
            field=models.ManyToManyField(to='testes.Tag', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teste',
            name='tags_2',
            field=models.CharField(max_length=100, null=True, verbose_name=testes.models.Tag, blank=True),
            preserve_default=True,
        ),
    ]
