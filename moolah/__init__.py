from django.conf import settings

if getattr(settings, 'BROKER_URL', None):
    from .celery import app as celery_app
