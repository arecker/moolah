# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allowance', '0003_auto_20150629_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='reason',
            field=models.IntegerField(default=0, choices=[(0, b'Allowance'), (1, b'Purchace'), (2, b'Refund'), (3, b'Penalty'), (4, b'Reward'), (5, b'Miscellaneous'), (6, b'Error')]),
        ),
    ]
