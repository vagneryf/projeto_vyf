# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0002_teste_mood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teste',
            name='mood',
        ),
        migrations.AddField(
            model_name='teste',
            name='tag',
            field=models.CharField(default=b'', help_text=b'Insira a tag', max_length=64),
            preserve_default=True,
        ),
    ]
