from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from os.path import join


class Theme(models.Model):
    name = models.CharField(max_length=60)
    url = models.URLField()

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    theme = models.ForeignKey(Theme, null=True, blank=True)
    buddy_icon = models.ImageField(
        upload_to='buddy_icons',
        null=True,
        blank=True
    )

    @property
    def buddy_icon_url(self):
        if self.buddy_icon:
            return join(settings.MEDIA_URL, self.buddy_icon.url)
        else:
            return None

    def __unicode__(self):
        return str(self.user)
