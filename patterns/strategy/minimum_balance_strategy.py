from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
 
class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    A strategy for applying service charges based on a minimum balance requirement.
    """
    SERVICE_CHARGE_PREMIUM: float = 2.0
   
    def __init__(self, minimum_balance: float):
        """
        Initializes the minimum balance strategy with the required balance.
        """
        self._minimum_balance = minimum_balance
       
    def calculate_service_charges(self, account: BankAccount)-> float:
        """
        Calculates service charges based on account balance:
        - If the balance meets or exceeds the minimum, apply the base service charge.
        - Otherwise, apply a premium service charge.
        """  
        if self._BankAccount__balance >= self._minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM  