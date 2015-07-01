# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import allowance.models


class Migration(migrations.Migration):

    dependencies = [
        ('allowance', '0006_auto_20150701_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='period',
            field=models.ForeignKey(default=allowance.models._get_latest_period, to='allowance.Period'),
        ),
    ]
