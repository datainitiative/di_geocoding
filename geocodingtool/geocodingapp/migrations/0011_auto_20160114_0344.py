# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0010_auto_20160111_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geocodingresult',
            name='location_type',
        ),
        migrations.RemoveField(
            model_name='geocodingresult',
            name='match_level',
        ),
        migrations.AddField(
            model_name='geocodingresult',
            name='accuracy',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geocodingresult',
            name='confidence_level',
            field=models.ForeignKey(blank=True, to='geocodingapp.ConfidenceLevel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geocodingresult',
            name='task',
            field=models.ForeignKey(default=0, to='geocodingapp.Task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.FileField(default='', max_length=500, upload_to=b'C:/QLiu/Devl/di_geocoding/geocodingtool/geocodingapp/static/data//upload/'),
            preserve_default=False,
        ),
    ]
