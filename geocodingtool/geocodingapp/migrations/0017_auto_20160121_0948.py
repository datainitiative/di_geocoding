# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0016_auto_20160121_0941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geocoder',
            options={'ordering': ['id']},
        ),
    ]
