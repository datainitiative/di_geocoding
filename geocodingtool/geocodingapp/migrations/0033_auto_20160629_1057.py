# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0032_task_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergeocodinglimit',
            name='last_geocoding_time',
            field=models.DateTimeField(null=True),
        ),
    ]
