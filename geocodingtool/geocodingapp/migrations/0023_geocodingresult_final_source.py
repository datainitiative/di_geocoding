# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocodingapp', '0022_finalsource'),
    ]

    operations = [
        migrations.AddField(
            model_name='geocodingresult',
            name='final_source',
            field=models.ForeignKey(default=1, to='geocodingapp.FinalSource'),
        ),
    ]
