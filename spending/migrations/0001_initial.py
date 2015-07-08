# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import spending.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthPeriod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('month', models.IntegerField(default=spending.models._get_month, choices=[(1, b'January'), (2, b'February'), (3, b'March'), (4, b'April'), (5, b'May'), (6, b'June'), (7, b'July'), (8, b'August'), (9, b'September'), (10, b'October'), (11, b'November'), (12, b'December')])),
                ('year', models.BigIntegerField(default=spending.models._get_year)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-year', '-month'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='monthperiod',
            unique_together=set([('month', 'year')]),
        ),
    ]
