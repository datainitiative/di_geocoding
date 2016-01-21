# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0017_auto_20160121_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='geocoderusage',
            name='has_expired',
            field=models.BooleanField(default=False),
        ),
    ]
