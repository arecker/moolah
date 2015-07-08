# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0002_auto_20150707_2308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlyperiod',
            options={'ordering': ['-year', '-month'], 'get_latest_by': 'date'},
        ),
    ]
