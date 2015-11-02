# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tracking.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=tracking.models.get_timestamp, editable=False),
        ),
    ]
