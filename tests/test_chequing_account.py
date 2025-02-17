Author = "Beerdavinder Singh"

import unittest
from datetime import date
from bank_account.chequing_account import Chequingaccount

class Testchequingaccount(unittest.TestCase):
    def setUp(self):
        """
        This is a setup of the attributes
        """
        self.chequing = Chequingaccount(700, 10, 100.00, date(2024, 10, 14), -100.00, 0.05)

    def test_invalid_overdraft_limit(self):
        """
        This is a invalid overdraft limit test
        """
        self.chequing = Chequingaccount(700, 10, 100.00, date(2024, 10, 14), "bs", 0.05)

    def test_invalid_overdraft_rate(self):
        """
        This is a test for invalid overdraft rate
        """
        self.chequing = Chequingaccount(700, 10, 100.00, date(2024, 10, 14), -100.00,"bs")

    def test_invalid_date(self):
        """
        This is a test for invalid date
        """
        self.chequing = Chequingaccount(700, 10, 100.00, "bs", -100.00, 0.05)

    def test_service_charge_greater_overdraft(self):
        """
        This is a test for service charge greater than overdraft
        """
        self.assertEqual(round(self.chequing.get_service_charges(), 2), 0.50)

    def test_service_charge_less_overdraft(self):
        """
        This is a test for service charge less than overdraft
        """
        self.chequing = Chequingaccount(700, 10, -200.00, date(2024, 10, 14), -100.00, 0.05)
        result_charge = 0.50 + (-100.00- -200.00) * 0.05
        self.assertEqual(round(self.chequing.get_service_charges(),2), 5.5)


    def test_service_charge_equal_overdraft(self):
        """
        This is a test for service charge equal to overdraft
        """
        self.chequing = Chequingaccount(700, 10, -100.00, date(2024, 10, 14), -100.00, 0.05)
        self.assertEqual(round(self.chequing.get_service_charges(),2), 0.50)

    def test_str_method(self):
        """
        This is a test for the string method
        """
        expected_str = (f"Account number: 700 Balance: $100.0\n"
                        "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% Account Type: Chequing")
        self.assertEqual(str(self.chequing), expected_str)