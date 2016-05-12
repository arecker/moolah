from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from pyexcel_ods import save_data


from tracking.models import Transaction


def send_email_with_export(recipient=None, path=None, body=None):
    body = body or 'Here are your exported transactions'
    email = EmailMessage('Transaction Export', body, None, [recipient, ])
    email.attach_file(path)
    email.send()


class Command(BaseCommand):
    help = 'exports negative transactions for the last month'

    def add_arguments(self, parser):
        parser.add_argument('--recipient')
        parser.add_argument('--path')
        parser.add_argument('--body')

    def handle(self, *args, **kwargs):
        recipient = kwargs.get('recipient', None)
        if not recipient:
            raise ValueError('need a recipient')

        path = kwargs.get('path', None)
        if not path:
            raise ValueError('need a path')

        transactions = Transaction.objects \
                                  .last_month() \
                                  .filter(amount__lt=0)

        sheet = [(t.timestamp.strftime('%m-%d-%Y'),
                  t.description,
                  str(t.amount)) for t in transactions]

        save_data(path, {'Sheet 1': sheet})
        send_email_with_export(recipient=recipient, path=path, body=kwargs.get('body', None))
