from django.test import TestCase
from django.contrib.auth.models import User


class UserAccountTests(TestCase):
    def test_account_create(self):
        """
        One account should be created
        for each new user
        """
        for u, p in [
                ('alex', 'Test1234'),
                ('marissa', 'Test5678'),
                ('ollie', 'TestWoof')
        ]:
            user = User.objects.create_user(u, p)
            user.save()
            self.assertIsNotNone(user.account)
