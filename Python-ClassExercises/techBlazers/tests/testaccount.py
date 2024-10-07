from unittest import TestCase

from classpractice import Account
from decimal import Decimal

class TestAccount(TestCase):
    def test_that_account_can_deposit(self):
        a1 = Account("Abimbs", "0000")
        a1.deposit(10000)
        a1.deposit(5000)
        self.assertEqual(a1.balance, 15000)