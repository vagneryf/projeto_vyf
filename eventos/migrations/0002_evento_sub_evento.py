# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='sub_evento',
            field=models.ForeignKey(blank=True, to='eventos.Evento', null=True),
            preserve_default=True,
        ),
    ]
