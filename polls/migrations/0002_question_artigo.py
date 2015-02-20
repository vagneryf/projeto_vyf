# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0004_auto_20150122_1518'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='artigo',
            field=models.ForeignKey(default=1, to='artigos.Artigo'),
            preserve_default=False,
        ),
    ]
