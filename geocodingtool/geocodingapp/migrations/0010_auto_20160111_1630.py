# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0009_task_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.FileField(max_length=500, null=True, upload_to=b'C:/QLiu/Devl/di_geocoding/geocodingtool/geocodingapp/static/data//upload/', blank=True),
            preserve_default=True,
        ),
    ]
