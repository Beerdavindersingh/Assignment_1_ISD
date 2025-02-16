Author = "Beerdavinder Singh"

import unittest
from datetime import date
from bank_account.chequing_account import Chequingaccount

class Testchequingaccount(unittest.TestCase):
    def setUp(self):
        """
        
        """
        self.chequing = Chequingaccount(700, 10, 100.00, date(2024, 10, 14), -100.00, 0.05)

    def test_invalid_overdraft_limit(self):
        """
        
        """
        self.chequing = Chequingaccount(700, 10, 100.00, date(2024, 10, 14), "bs", 0.05)

    def test_invalid_overdraft_rate(self):
        """
        
        """
        self.chequing = Chequingaccount(700, 10, 100.00, date(2024, 10, 14), -100.00,"bs")

    def test_invalid_date(self):
        """
        
        """
        self.chequing = Chequingaccount(700, 10, 100.00, "bs", -100.00, 0.05)

    def test_service_charge_greater_overdraft(self):
        """
        
        """
        self.assertEqual(round(self.chequing.get_service_charges(), 2), 0.50)

    def test_service_charge_less_overdraft(self):
        """
        
        """
        self.chequing = Chequingaccount(700, 10, -200.00, date(2024, 10, 14), -100.00, 0.05)
        result_charge = 0.50 + (-100.00- -200.00) * 0.05
        self.assertEqual(round(self.chequing.get_service_charges(),2), 5.5)


    def test_service_charge_equal_overdraft(self):
        """
        
        """
        self.chequing = Chequingaccount(700, 10, -100.00, date(2024, 10, 14), -100.00, 0.05)
        self.assertEqual(round(self.chequing.get_service_charges(),2), 0.50)

    def test_str_method(self):
        """
        
        """
        expected_str = (f"Account number: 700 Balance: $100.0\n"
                        "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% Account Type: Chequing")
        self.assertEqual(str(self.chequing), expected_str)