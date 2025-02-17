from datetime import date
from bank_account.bank_account import BankAccount
 
class SavingAccount(BankAccount):
   
    SERVICE_CHARGE_PREMIUM = 2.00
   
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        """
        attributes: minimun balance(float)
        """
       
        super().__init__(account_number, client_number, balance, date_created)
       
        try:
            self.__minimum_balance = float(minimum_balance)
        except:
            self.__minimum_balance = 50.00
           
    @property
    def minimum_balance(self):
        """
        this will return minimum balance 
        """
        return self.__minimum_balance
   
    def __str__(self) -> str:
        """
        this is a def for the formatted string
        """
        return (f"{super().__str__()}\n"
                f"Minimum Balance: ${self.__minimum_balance:.2f} Account Type: Savings")
                         
    def get_service_charges(self):
        """
        this is a def for get service charges
        """
        if self._balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
                             
