# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0011_auto_20160114_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formattedaddress',
            name='city',
            field=models.ForeignKey(blank=True, to='geocodingapp.City', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formattedaddress',
            name='county',
            field=models.ForeignKey(blank=True, to='geocodingapp.County', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formattedaddress',
            name='state',
            field=models.ForeignKey(blank=True, to='geocodingapp.State', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='geocodingresult',
            name='address',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='geocodingresult',
            name='formatted_address',
            field=models.ForeignKey(blank=True, to='geocodingapp.FormattedAddress', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='geocodingresult',
            name='geocoder',
            field=models.ForeignKey(blank=True, to='geocodingapp.Geocoder', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='geocodingresult',
            name='location',
            field=models.ForeignKey(blank=True, to='geocodingapp.Point', null=True),
            preserve_default=True,
        ),
    ]
