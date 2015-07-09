from django.test import TestCase
from django.contrib.auth.models import User
from .models import MonthlyPeriod, MonthlyTransaction, MonthlyBudget
from decimal import Decimal


class TransactionManagerTests(TestCase):
    def setUp(self):
        self.period = MonthlyPeriod()
        self.period.save()
        self.user = User.objects.create_user('hal', 'testpass')
        self.user.save()
        self.budget = MonthlyBudget()
        self.budget.name = 'TestBudget'
        self.budget.allowance = Decimal(100)
        self.budget.save()

    def test_sanity_balance(self):
        """
        should calculate the balance of
        one positive trasaction
        """
        t1 = MonthlyTransaction()
        t1.negative = False
        t1.period = self.period
        t1.user = self.user
        t1.amount = Decimal(10)
        t1.budget = self.budget
        t1.save()

        actual = MonthlyTransaction.objects.balance()
        expected = Decimal(10)
        self.assertEqual(actual, expected)

    def test_sanity_negative(self):
        """
        should calculate balance of
        one negative number
        """
        t1 = MonthlyTransaction()
        t1.negative = True
        t1.period = self.period
        t1.user = self.user
        t1.amount = Decimal(10)
        t1.budget = self.budget
        t1.save()

        actual = MonthlyTransaction.objects.balance()
        expected = Decimal(-10)
        self.assertEqual(actual, expected)

    def test_sanity_mixed(self):
        """
        should calculate balance of
        one negative number and one positive
        number
        """
        t1 = MonthlyTransaction()
        t1.negative = True
        t1.period = self.period
        t1.user = self.user
        t1.amount = Decimal(10)
        t1.budget = self.budget
        t1.save()

        t2 = MonthlyTransaction()
        t2.negative = False
        t2.period = self.period
        t2.user = self.user
        t2.amount = Decimal(5)
        t2.budget = self.budget
        t2.save()

        actual = MonthlyTransaction.objects.balance()
        expected = Decimal(-5)
        self.assertEqual(actual, expected)

    def test_sanity_filter(self):
        """
        should only make calculations based on filter
        """
        t1 = MonthlyTransaction()
        t1.negative = True
        t1.period = self.period
        t1.user = self.user
        t1.amount = Decimal(10)
        t1.budget = self.budget
        t1.save()

        t2 = MonthlyTransaction()
        t2.negative = False
        t2.period = self.period
        t2.user = self.user
        t2.amount = Decimal(5)
        t2.budget = self.budget
        t2.save()

        actual = MonthlyTransaction.objects.filter(
            negative=True
        ).balance()
        expected = Decimal(-10)
        self.assertEqual(actual, expected)


class MonthlyTransactionManagerTests(TestCase):
    def setUp(self):
        self.period = MonthlyPeriod()
        self.period.save()
        self.user = User.objects.create_user('hal', 'testpass')
        self.user.save()
        self.budget = MonthlyBudget()
        self.budget.name = 'Test Budget'
        self.budget.allowance = Decimal(100)
        self.budget.save()

    def test_latest_period(self):
        """
        should fetch all transactions for 1 budget for the latest period
        """
        t1 = MonthlyTransaction()
        t1.description = 'Test'
        t1.amount = Decimal(10)
        t1.negative = True
        t1.budget = self.budget
        t1.period = self.period
        t1.user = self.user
        t1.save()

        transactions = MonthlyTransaction.objects.latest_period(
            budget=self.budget)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions.first().amount, Decimal(10))
        self.assertEqual(transactions.balance(), Decimal(-10))
