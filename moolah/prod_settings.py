import os

from settings import *


INSTALLED_APPS += ("djcelery_email",)

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = [
    os.environ['HOST'],
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moolah',
        'USER': 'postgres',
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': 'db',
    }
}

STATIC_ROOT = '/var/www/moolah/static/'
MEDIA_ROOT = '/var/www/moolah/media/'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": 'redis://redis:6739/1',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

BROKER_URL = 'redis://redis:6379/2'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = os.environ.get('CELERY_TIMEZONE', 'America/Chicago')

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
# EMAIL_HOST = os.environ['EMAIL_HOST']
# EMAIL_HOST_USER = os.environ['EMAIL_USER']
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
# EMAIL_PORT = os.environ['EMAIL_PORT']
# EMAIL_USE_TLS = True
