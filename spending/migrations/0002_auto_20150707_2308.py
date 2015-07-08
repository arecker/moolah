# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlyperiod',
            options={'ordering': ['-year', '-month'], 'get_latest_by': ['date']},
        ),
    ]
