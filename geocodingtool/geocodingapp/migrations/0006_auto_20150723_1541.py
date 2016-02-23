# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0005_auto_20150723_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['city']},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ['geoid']},
        ),
        migrations.RemoveField(
            model_name='city',
            name='county',
        ),
    ]
