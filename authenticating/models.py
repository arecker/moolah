from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
import uuid


class Theme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    url = models.URLField(unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name', ]


class Account(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    theme = models.ForeignKey(Theme, null=True, blank=True)

    @property
    def name(self):
        return self.user.get_full_name() or self.user.get_username()

    def __unicode__(self):
        return self.name
