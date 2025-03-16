from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta
 
class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    A strategy for applying management fees to service charges.
    """
   
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
 
    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the management fee strategy with the account creation date and fee.
        """
        self._date_created = date_created
        self._management_fee = management_fee
       
    def calculate_service_charges(self, account: BankAccount)-> float:
        """
        Calculates the service charges based on account age.
        - If the account is older than 10 years: apply base service charge.
        - Otherwise: add the management fee to the base service charge.
        """
        if self._date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
           
        else:
            return self.BASE_SERVICE_CHARGE + self._management_fee