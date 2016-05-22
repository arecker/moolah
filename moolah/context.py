from django.conf import settings


def debug(*args, **kwargs):
    return {'DEBUG': getattr(settings, 'DEBUG', False)}
