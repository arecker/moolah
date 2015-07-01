# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allowance', '0005_period_closed'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='period',
            unique_together=set([('month', 'year')]),
        ),
    ]
