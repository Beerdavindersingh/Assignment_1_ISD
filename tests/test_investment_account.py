import unittest
from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from bank_account.investment_account import InvestmentAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
 
class TestInvestmentAccount(unittest.TestCase):
   
    def setUp(self):
        """
        This is a test setup
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, date.today(), 4.00)
        self.eleven_years_ago = date.today() - timedelta(days=11*365.25)
        self.exactly_ten_years_ago = date.today() - timedelta(days=10*365.25)
        self.eight_years_ago = date.today() - timedelta(days=8*365.25)
       
    def test_parameter_values_set(self):
        """
        This is a test for the attributes
        """
        self.assertEqual(self.investment.account_number, 22222)
        self.assertEqual(self.investment.client_number, 3333)
        self.assertEqual(self.investment.balance, 4444.44)
        self.assertEqual(self.investment.date_created, date.today())
        self.assertEqual(self.investment.management_fee, 4.00)
       
    def test_management_fee_invalid(self):
        """
        This is a test for the invalid management fee
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, date.today(), "invalid")
        self.assertEqual(2.55, round(self.investment.management_fee, 2))
   
    def test_date_more_than_10_years(self):
        """
        This is a test for date more than 10 years
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.eleven_years_ago, 4.00)
        expected_charge = ManagementFeeStrategy(self.eleven_years_ago,4.00) .calculate_service_charges(self.investment)
        self.assertEqual(expected_charge, self.investment.get_service_charges())      
   
    def test_date_exactly_ten_years_ago(self):
        """
        This is a test for date exact ten years
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.exactly_ten_years_ago, 4.00)
        ten_years_ago = InvestmentAccount(2005, 22, 100.00, date.today(), 4.00)
        self.assertEqual(round(self.investment.get_service_charges(), 2), 0.5)
       
    def test_date_within_last_ten_years(self):
        """
        This is test for date within ten years
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.eight_years_ago, 4.00)
        self.assertEqual(round(self.investment.get_service_charges(), 2),4.5)
       
    def test_display_waived_more_than_ten_years(self):
        """
        This is a test for date more than 10 years
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.eleven_years_ago, 4.00)
        expected = f"Account number: 22222 Balance: $4444.44\n" \
                   f"Management Fee: Waived Account Type: Investment"
        self.assertEqual(str(self.investment), expected)  
       
    def test_display_waived_within_ten_years(self):
        """
        This is a test for waived within 10 years
        """
        self.investment = InvestmentAccount(22222, 3333, 4444.44, self.eight_years_ago, 4.00)
        expected = f"Account number: 22222 Balance: $4444.44\n" \
                   f"Management Fee: $4.00 Account Type: Investment"
        self.assertEqual(str(self.investment), expected)
