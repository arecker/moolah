# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import moolah.utils


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=moolah.utils.get_timestamp),
        ),
    ]
