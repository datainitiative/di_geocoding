# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0018_geocoderusage_has_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='formattedaddress',
            name='geocoder',
            field=models.ForeignKey(blank=True, to='geocodingapp.Geocoder', null=True),
        ),
    ]
