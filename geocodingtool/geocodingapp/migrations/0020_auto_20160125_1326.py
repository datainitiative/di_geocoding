# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0019_formattedaddress_geocoder'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('formatted_address', models.ForeignKey(blank=True, to='geocodingapp.FormattedAddress', null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'address_inventory',
            },
        ),
        migrations.RemoveField(
            model_name='address',
            name='task',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
