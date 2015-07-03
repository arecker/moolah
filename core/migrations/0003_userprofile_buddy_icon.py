# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150703_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='buddy_icon',
            field=models.ImageField(null=True, upload_to=b'buddy_icons', blank=True),
        ),
    ]
