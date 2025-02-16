Author = "Beerdavinder Singh"

from datetime import date
from bank_account.bank_account import BankAccount

class Chequingaccount(BankAccount):
    def _init_(self, account_number:int, client_number:int, balance: float, date_created: date, overdraft_limit:float, overdraft_rate: float):
        """
        
        """
        super()._init_(account_number, client_number, balance, date_created)
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.0

        try: 
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.5

    @property
    def overdraft_limit(self):
        return self.__overdraft_limit
    
    @property
    def overdraft_rate(self):
        return self.__overdraft_rate
    
    def _str_(self):
        """
        
        """
        major_strg = super()._str_()
        return (f"{major_strg}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f} "
                f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}% "
                f"Account Type: Chequing")
        
    def get_service_charges(self):
        """
        
        """
        if self._BankAccount__balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + ((self.__overdraft_limit - self._BankAccount__balance) * self.__overdraft_rate)