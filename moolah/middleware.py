import pytz

from django.utils import timezone


class TimezoneMiddleware(object):
    def process_request(self, *args):
        timezone.activate(pytz.timezone('America/Chicago'))
