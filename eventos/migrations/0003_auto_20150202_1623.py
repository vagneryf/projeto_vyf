# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_sub_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(default=datetime.datetime(2015, 2, 2, 18, 23, 8, 999000, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
