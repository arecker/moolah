# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields
import uuid


def load_themes(*args):
    from scripts.load_bootswatch_themes import run
    run()


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(null=True, upload_to=b'avatars/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='account',
            name='theme',
            field=models.ForeignKey(blank=True, to='authenticating.Theme', null=True),
        ),

        migrations.RunPython(load_themes)
    ]
