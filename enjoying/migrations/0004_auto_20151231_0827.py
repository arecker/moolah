# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import moolah.utils


class Migration(migrations.Migration):

    dependencies = [
        ('enjoying', '0003_auto_20151109_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='timestamp',
            field=models.DateTimeField(default=moolah.utils.get_timestamp),
        ),
    ]
