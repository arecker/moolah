from decimal import Decimal

from django.test import TestCase

from models import Rate, Transaction


def to_decimal(amount, place='0.001'):
    return Decimal(amount).quantize(Decimal(place))


class TestRate(TestCase):
    def setUp(self):
        self.rate1 = Rate()
        self.rate1.description = 'Test 1'
        self.rate1.amount = -50
        self.rate1.days = 30
        self.rate1.save()
        self.rate1.refresh_from_db()

        self.rate2 = Rate()
        self.rate2.description = 'Test 2'
        self.rate2.amount = -100
        self.rate2.days = 30
        self.rate2.save()
        self.rate2.refresh_from_db()

        self.rate3 = Rate()
        self.rate3.description = 'Test 3'
        self.rate3.amount = 100
        self.rate3.days = 5
        self.rate3.save()
        self.rate3.refresh_from_db()

    def test_amount_per_day(self):
        self.assertEqual(self.rate1.amount_per_day, to_decimal(-1.667))
        self.assertEqual(self.rate2.amount_per_day, to_decimal(-3.333))
        self.assertEqual(self.rate3.amount_per_day, to_decimal(20))

    def test_total(self):
        self.assertEqual(Rate.objects.total(),
                         to_decimal(15))


class TestTransaction(TestCase):
    def setUp(self):
        self.test1 = Transaction()
        self.test1.description = 'Test1'
        self.test1.amount = to_decimal(-5, place='0.01')
        self.test1.save()
        self.test1.refresh_from_db()

        self.test2 = Transaction()
        self.test2.description = 'Test2'
        self.test2.amount = to_decimal(-10, place='0.01')
        self.test2.save()
        self.test2.refresh_from_db()

        self.test3 = Transaction()
        self.test3.description = 'Test3'
        self.test3.amount = to_decimal(1.2, place='0.01')
        self.test3.save()
        self.test3.refresh_from_db()

    def test_today_count(self):
        todays = Transaction.objects.today()
        self.assertEqual(todays.count(), 3)

    def test_today_total(self):
        total = Transaction.objects.today().total()
        self.assertEqual(total, to_decimal(-13.8, place='0.01'))


class TestTransactRateBalance(TestCase):
    def setUp(self):
        self.rate1 = Rate()
        self.rate1.description = 'Test 1'
        self.rate1.amount = -50
        self.rate1.days = 30
        self.rate1.save()
        self.rate1.refresh_from_db()

        self.rate2 = Rate()
        self.rate2.description = 'Test 2'
        self.rate2.amount = -100
        self.rate2.days = 30
        self.rate2.save()
        self.rate2.refresh_from_db()

    def test_transaction(self):
        Transaction.objects.transact_rate_balance()
        self.assertEqual(Transaction.objects.total(),
                         to_decimal(-5, place='0.01'))
