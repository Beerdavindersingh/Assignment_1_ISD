Author = "Beerdavinder Singh"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
 
 
class InvestmentAccount(BankAccount):
   
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
   
    def __init__(self, account_number: int, client_number: int, balance: int,
                 date_created: date, mangement_fee: float):
        """
         
            
        """
 
        super().__init__(account_number, client_number, balance, date_created)
       
        try:
            self.__management_fee = float(mangement_fee)
        except(ValueError):
            self.__management_fee = 2.55
            """
            .
            """
           
    @property
    def management_fee(self):
        """
       
        """
        return self.__management_fee
   
    def __str__(self) -> str:
        """
        .
        """
        if self._BankAccount__date_created >= self.TEN_YEARS_AGO:
            management_fee = f"${self.__management_fee:.2f}"
        else:
            management_fee = "Waived"
           
        return (f"{super().__str__()}\n"
               f"Management Fee: {management_fee} Account Type: Investment")
       
       
    def get_service_charges(self) -> float:
        """
        
        """
        if self._BankAccount__date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
           
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee