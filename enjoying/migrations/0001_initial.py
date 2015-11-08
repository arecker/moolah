# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import moolah.utils
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, unique=True)),
                ('description', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(default=moolah.utils.get_timestamp, editable=False)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
                'abstract': False,
            },
        ),
    ]
