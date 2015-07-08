# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import spending.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPeriod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
                ('month', models.IntegerField(default=spending.models._get_month, choices=[(1, b'January'), (2, b'February'), (3, b'March'), (4, b'April'), (5, b'May'), (6, b'June'), (7, b'July'), (8, b'August'), (9, b'September'), (10, b'October'), (11, b'November'), (12, b'December')])),
                ('year', models.BigIntegerField(default=spending.models._get_year)),
                ('date', models.DateTimeField(null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ['-year', '-month'],
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='MonthlyTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('negative', models.BooleanField(default=False)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('description', models.CharField(max_length=120, null=True, blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
                ('period', models.ForeignKey(to='spending.MonthlyPeriod')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='monthlyperiod',
            unique_together=set([('month', 'year')]),
        ),
    ]
