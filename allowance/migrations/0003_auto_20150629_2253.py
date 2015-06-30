# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allowance', '0002_auto_20150629_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ['-year', '-month']},
        ),
    ]
