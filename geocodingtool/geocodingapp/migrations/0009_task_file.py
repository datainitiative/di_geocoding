# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0008_auto_20160103_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(null=True, upload_to=b'C:/QLiu/Devl/di_geocoding/geocodingtool/geocodingapp/static/data//upload/', blank=True),
            preserve_default=True,
        ),
    ]
