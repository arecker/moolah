# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlytransaction',
            name='reason',
            field=models.IntegerField(default=1, choices=[(0, b'Allowance'), (1, b'Purchase'), (2, b'Refund'), (3, b'Penalty'), (4, b'Reward'), (5, b'Adjustment'), (6, b'Error'), (7, b'Other')]),
        ),
    ]
