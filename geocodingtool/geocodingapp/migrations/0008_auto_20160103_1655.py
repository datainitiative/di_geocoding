# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0007_city_geoid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formattedaddresstopoint',
            name='confidence_level',
        ),
        migrations.RemoveField(
            model_name='formattedaddresstopoint',
            name='formatted_address',
        ),
        migrations.RemoveField(
            model_name='formattedaddresstopoint',
            name='point',
        ),
        migrations.DeleteModel(
            name='FormattedAddressToPoint',
        ),
        migrations.AddField(
            model_name='formattedaddress',
            name='confidence_level',
            field=models.ForeignKey(blank=True, to='geocodingapp.ConfidenceLevel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formattedaddress',
            name='point',
            field=models.ForeignKey(blank=True, to='geocodingapp.Point', null=True),
            preserve_default=True,
        ),
    ]
