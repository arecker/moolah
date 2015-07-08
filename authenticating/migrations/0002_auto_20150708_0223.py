# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='theme',
            field=models.ForeignKey(blank=True, to='authenticating.Theme', null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
