import unittest
from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from bank_account.investment_account import InvestmentAccount
 
class TestInvestmentAccount(unittest.TestCase):
   
    def setUp(self):
        """
        
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, date.today(), 4.00)
        self.eleven_years_ago = date.today() - timedelta(days=11*365.25)
        self.exactly_ten_years_ago = date.today() - timedelta(days=10*365.25)
        self.eight_years_ago = date.today() - timedelta(days=8*365.25)
       
    def test_parameter_values_set(self):
        """
        
        """
        self.assertEqual(self.investment.account_number, 22222)
        self.assertEqual(self.investment.client_number, 3333)
        self.assertEqual(self.investment.balance, 4444.44)
        self.assertEqual(self.investment.date_created, date.today())
        self.assertEqual(self.investment.management_fee, 4.00)
       
    def test_management_fee_invalid(self):
        """
        
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, date.today(), "invalid")
        self.assertEqual(2.55, round(self.investment.management_fee, 2))
   
    def test_date_more_than_10_years(self):
        """
        
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.eleven_years_ago, 4.00)
        self.assertEqual(InvestmentAccount.BASE_SERVICE_CHARGE, self.investment.get_service_charges())      
   
    def test_date_exactly_ten_years_ago(self):
        """
        
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.exactly_ten_years_ago, 4.00)
        self.assertEqual(InvestmentAccount.BASE_SERVICE_CHARGE, self.investment.get_service_charges())
       
    def test_date_within_last_ten_years(self):
        """
        
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.eight_years_ago, 4.00)
        self.assertEqual(InvestmentAccount.BASE_SERVICE_CHARGE + 4.0, self.investment.get_service_charges())
       
    def test_display_waived_more_than_ten_years(self):
        """
        
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.eleven_years_ago, 4.00)
        expected = f"Account number: 22222 Balance: $4444.44\n" \
                   f"Management Fee: Waived Account Type: Investment"
        self.assertEqual(str(self.investment), expected)  
       
    def test_display_waived_within_ten_years(self):
        """
        
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.eight_years_ago, 4.00)
        expected = f"Account number: 22222 Balance: $4444.44\n" \
                   f"Management Fee: $4.00 Account Type: Investment"
        self.assertEqual(str(self.investment), expected)
