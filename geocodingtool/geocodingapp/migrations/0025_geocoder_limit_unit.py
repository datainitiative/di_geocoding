# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0024_formattedaddress_accuracy'),
    ]

    operations = [
        migrations.AddField(
            model_name='geocoder',
            name='limit_unit',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
