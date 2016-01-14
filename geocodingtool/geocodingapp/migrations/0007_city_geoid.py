# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0006_auto_20150723_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='geoid',
            field=models.CharField(default='08', max_length=7),
            preserve_default=False,
        ),
    ]
