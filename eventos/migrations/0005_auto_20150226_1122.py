# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import eventos.models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20150226_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_fim',
            field=models.DateTimeField(default=eventos.models.mais_quinze, verbose_name='Data fim (m\xedn = 15min)', blank=True),
            preserve_default=True,
        ),
    ]
