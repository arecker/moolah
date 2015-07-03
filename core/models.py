from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    name = models.CharField(max_length=60)
    url = models.URLField()

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    theme = models.ForeignKey(Theme, null=True, blank=True)

    def __unicode__(self):
        return str(self.user)
