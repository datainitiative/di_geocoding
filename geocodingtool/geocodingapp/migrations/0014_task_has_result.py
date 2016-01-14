# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0013_geocodingresult_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='has_result',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
