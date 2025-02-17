import unittest
from datetime import date
from bank_account.bank_account import BankAccount
from bank_account.savings_account import SavingAccount
 
class TestSavingAccount(unittest.TestCase):
   
    def setUp(self):
        """
        
        """
        self.saving = SavingAccount(22222, 3333, 4444.44, date.today(), 250.00)
         
    def test_attribute_set_to_parameter_values(self):
        """
        
        """
        self.assertEqual(self.saving.account_number, 22222)
        self.assertEqual(self.saving.client_number, 3333)
        self.assertEqual(self.saving.balance, 4444.44)
        self.assertEqual(self.saving.date_created, date.today())
        self.assertEqual(self.saving.minimum_balance, 250.00)
       
    def test_invalid_minimum_balance(self):
        """
        
        """
        self.saving = SavingAccount(22222, 3333, 4444.44, date.today(), "invalid")
        self.assertEqual(50.00, round(self.saving.minimum_balance, 2))
   
    def test_balance_greater(self):
        """
        
        """
        self.saving = SavingAccount(22222, 3333, 4444.44, date.today(), 250.00)
        self.assertEqual(self.saving.BASE_SERVICE_CHARGE, self.saving.get_service_charges())
       
    def test_balance_equal(self):
        """
        
        """
        self.saving = SavingAccount(22222, 3333, 250.00, date.today(), 250.00)
        self.assertEqual(self.saving.BASE_SERVICE_CHARGE, self.saving.get_service_charges())    
   
    def test_balance_less(self):
        """
        
        """
        self.saving = SavingAccount(22222, 3333, 44.44, date.today(), 250.00)
        self.assertEqual(self.saving.BASE_SERVICE_CHARGE * self.saving.SERVICE_CHARGE_PREMIUM, self.saving.get_service_charges())    
   
    def test_str_representation(self):
        """
        
        """
        self.saving = SavingAccount(22222, 3333, 4444.44, date.today(), 250.00)
       
        expected = f"Account number: 22222 Balance: $4444.44\n" \
                   f"Minimum Balance: $250.00 Account Type: Savings"
                   
        self.assertEqual(str(self.saving), expected)          
       
                             