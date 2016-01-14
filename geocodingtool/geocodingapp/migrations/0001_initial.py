# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('upload_table', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'city',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfidenceLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'confidence_level',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geoid', models.CharField(max_length=5)),
                ('county', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'county',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormattedAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=500, null=True, blank=True)),
                ('street_number', models.CharField(max_length=250, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=5, null=True, blank=True)),
                ('city', models.ForeignKey(to='geocodingapp.City')),
                ('county', models.ForeignKey(to='geocodingapp.County', null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'formatted_address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormattedAddressToPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confidence_level', models.ForeignKey(to='geocodingapp.ConfidenceLevel')),
                ('formatted_address', models.ForeignKey(to='geocodingapp.FormattedAddress')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'formatted_address_to_point',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Geocoder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'geocoder',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeocodingResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.ForeignKey(to='geocodingapp.Address')),
                ('formatted_address', models.ForeignKey(to='geocodingapp.FormattedAddress')),
                ('geocoder', models.ForeignKey(to='geocodingapp.Geocoder')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'geocoding_result',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'location_type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MatchLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'match_level',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
            options={
                'db_table': 'point',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500, null=True, blank=True)),
                ('url', models.URLField(max_length=5000, null=True, blank=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'project',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'project_category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geoid', models.CharField(max_length=2)),
                ('state', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'state',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('note', models.TextField(max_length=500, null=True, blank=True)),
                ('project', models.ForeignKey(to='geocodingapp.Project')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'task',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(to='geocodingapp.ProjectCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geocodingresult',
            name='location',
            field=models.ForeignKey(to='geocodingapp.Point'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geocodingresult',
            name='location_type',
            field=models.ForeignKey(to='geocodingapp.LocationType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geocodingresult',
            name='match_level',
            field=models.ForeignKey(to='geocodingapp.MatchLevel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formattedaddresstopoint',
            name='point',
            field=models.ForeignKey(to='geocodingapp.Point'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formattedaddress',
            name='state',
            field=models.ForeignKey(to='geocodingapp.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(to='geocodingapp.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='county',
            field=models.ForeignKey(to='geocodingapp.County', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='geocodingapp.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='task',
            field=models.ForeignKey(to='geocodingapp.Task'),
            preserve_default=True,
        ),
    ]
