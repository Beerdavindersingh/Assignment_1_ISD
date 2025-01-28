"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """
        This is the setup for tests
        """
        self.Bank_account = BankAccount(700, 10, 100.00)
    
    def test_invalid_account_number(self):
        """
        this def will raise a error if the account number is no valid
        """
        with self.assertRaises(ValueError):
            self.Bank_account = BankAccount("bd", 10 , 100.00)
    
    def test_invalid_client_number(self):
        """
        this def will raisse a error if the client number is not a integar
        """
        with self.assertRaises(ValueError):
            self.Bank_account = BankAccount(700,"bd",100.00)

    def test_invalid_balance(self):
        """
        this def will raise a error if the balance is invalid
        """ 
        self.Bank_account = BankAccount(700, 10 , "bd")
        self.assertEqual(round(self.Bank_account.balance, 2), 0.0)


    def test_account_number(self):
        """
        this def will return the account number
        """
        self.assertEqual(self.Bank_account.account_number, 700)

    def test_client_number(self):
        """
        this def will return the client number
        """
        self.assertEqual(self.Bank_account.client_number, 10)

    def test_balance(self):
        """
        this def will return the balance 
        """
        self.assertEqual(round(self.Bank_account.balance, 2), 100.00)
    
    def test_valid_deposit_amount(self):
        """
        this def will test the valid deposit amount
        """
        self.Bank_account.deposit(100.00)
        self.assertEqual(round(self.Bank_account.balance, 2), 200.00)

    def test_non_numeric_deposit(self):
        """
        this def will raise a error if the deposit is not numeric
        """
        with self.assertRaises(ValueError):
            self.Bank_account.deposit("bd")

    def test_not_positive_deposit(self):
        """
        this def will rasise a error if the deposit amount is not a positive number
        """
        with self.assertRaises(ValueError):
            self.Bank_account.deposit(-50.00)

    def test_update_balance_positive(self):
        """
        this def will update the balance in positive
        """
        self.Bank_account.update_balance(50.00)
        self.assertEqual(round(self.Bank_account.balance, 2), 150.00)

    def test_update_balance_negative(self):
        """
        this def will update the balance in negative
        """
        self.Bank_account.update_balance(-50.00)
        self.assertEqual(round(self.Bank_account.balance, 2), 50.00)

    def test_update_balance_non_numeric(self):
        """
        this def will not update the balane if the balance is non numeric
        """
        balance = self.Bank_account.balance
        self.Bank_account.update_balance("bd")
        self.assertEqual(self.Bank_account.balance, balance)

    def test_valid_withdraw(self):
        """
        this def will test the valid withdraw
        """
        self.Bank_account.withdraw(50.00)
        self.assertEqual(round(self.Bank_account.balance,2), 50.00)

    def test_invalid_withdraw_negative(self):
        """
        this def will raise a error if the withdraw is in negative
        """
        with self.assertRaises(ValueError):
            self.Bank_account.withdraw(-50.00)

    def test_withdraw_exceeds_balance(self):
        """
        this def will raise a error if the withdraw exceeds the balance
        """
        with self.assertRaises(ValueError):
            self.Bank_account.withdraw(200.00)    
    
    def test_non_numeric_withdraw(self):
        """
        This def will raise a error if the withdraw is non numeric
        """
        with self.assertRaises(ValueError):
            self.Bank_account.withdraw("bd")

    def test_str_method(self):
        """
        this def is for str method that will give the result in format
        """
        expected_str = "Account number: 700 Balance: $100.0"
        self.assertEqual(str(self.Bank_account), expected_str)