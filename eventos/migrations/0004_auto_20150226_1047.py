# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import eventos.models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20150202_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_fim',
            field=models.DateTimeField(default=eventos.models.mais_quinze, verbose_name='Data fim (m\xedn = 15min)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data in\xedcio', blank=True),
            preserve_default=True,
        ),
    ]
