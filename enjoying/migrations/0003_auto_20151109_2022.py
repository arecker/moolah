# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enjoying', '0002_auto_20151108_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user',
        ),
        migrations.AddField(
            model_name='purchase',
            name='allowance',
            field=models.ForeignKey(to='enjoying.Allowance', null=True),
        ),
    ]
