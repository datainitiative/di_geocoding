# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0014_task_has_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeocoderUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_geocoding_record_num', models.IntegerField(default=0)),
                ('last_geocoding_time', models.DateTimeField(auto_now=True)),
                ('geocoder', models.ForeignKey(to='geocodingapp.Geocoder')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'geocoder_usage',
            },
        ),
        migrations.RemoveField(
            model_name='formattedaddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='formattedaddress',
            name='county',
        ),
        migrations.RemoveField(
            model_name='formattedaddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='formattedaddress',
            name='street_name',
        ),
        migrations.RemoveField(
            model_name='formattedaddress',
            name='street_number',
        ),
        migrations.RemoveField(
            model_name='formattedaddress',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='task',
            name='initiate_date',
            field=models.DateField(auto_now=True),
        ),
    ]
