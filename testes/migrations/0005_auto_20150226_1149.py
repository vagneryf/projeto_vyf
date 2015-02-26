# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0004_auto_20150226_1138'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Tag',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'tags'},
        ),
        migrations.RenameField(
            model_name='teste',
            old_name='categories',
            new_name='tags',
        ),
        migrations.RemoveField(
            model_name='teste',
            name='tag',
        ),
    ]
