# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0015_auto_20160120_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geocoderusage',
            old_name='last_geocoding_record_num',
            new_name='geocoding_record_num',
        ),
        migrations.AddField(
            model_name='geocoder',
            name='limit',
            field=models.IntegerField(default=-1),
        ),
    ]
