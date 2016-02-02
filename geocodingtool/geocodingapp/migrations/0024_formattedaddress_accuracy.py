# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0023_geocodingresult_final_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='formattedaddress',
            name='accuracy',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
