Author = "Beerdavinder Singh"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class Chequingaccount(BankAccount):
    def __init__(self, account_number:int, client_number:int, balance: float, date_created: date, overdraft_limit:float, overdraft_rate: float):
        """
        Attributes:
            Account number (int)
            Client number (int)
            balance (float)
            date created (Date)
            overdraft_limit(float)
            overdraft rate(float)
        """
        super().__init__(account_number, client_number, balance, date_created)
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.0

        try: 
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.5

        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit
    
    @property
    def overdraft_rate(self):
        return self.__overdraft_rate
    
    def __str__(self):
        """
        This is a def for a fomat of a string that we want to get as a result
        """
    
        return (f"{super().__str__()}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f} Overdraft Rate: {self.__overdraft_rate * 100:.2f}% Account Type: Chequing")
        
    def get_service_charges(self) -> float:
        """
        This is a def to get the service charge as a result
        """
        return self.__strategy.calculate_service_charges(self)