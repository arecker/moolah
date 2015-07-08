# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0003_auto_20150707_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyperiod',
            name='date',
            field=models.DateTimeField(null=True, editable=False, blank=True),
        ),
    ]
