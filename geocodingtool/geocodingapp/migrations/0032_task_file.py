# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0031_remove_task_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(default=' ', max_length=500, upload_to=b'C:/QLiu/Devl/di_geocoding/geocodingtool/geocodingapp/static/data//upload/'),
            preserve_default=False,
        ),
    ]
