# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(null=True, blank=True)),
                ('allowance', models.DecimalField(max_digits=6, decimal_places=2)),
                ('shared', models.BooleanField(default=False)),
                ('reoccuring', models.IntegerField(choices=[(0, b'Weekly'), (1, b'Monthly')])),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
                ('start', models.DateField(default=django.utils.timezone.now)),
                ('end', models.DateField(null=True, blank=True)),
                ('reoccuring', models.IntegerField(choices=[(0, b'Weekly'), (1, b'Monthly')])),
            ],
            options={
                'ordering': ['-start'],
                'get_latest_by': 'start',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('reason', models.IntegerField(default=1, choices=[(0, b'Allowance'), (1, b'Purchase'), (2, b'Refund'), (3, b'Penalty'), (4, b'Reward'), (5, b'Adjustment'), (6, b'Error'), (7, b'Other')])),
                ('negative', models.BooleanField(default=False)),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
                ('description', models.CharField(max_length=120, null=True, blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
                ('budget', models.ForeignKey(to='spending.Budget')),
                ('period', models.ForeignKey(to='spending.Period')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
