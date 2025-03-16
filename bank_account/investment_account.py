Author = "Beerdavinder Singh"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
 
 
class InvestmentAccount(BankAccount):
   
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
   
    def __init__(self, account_number: int, client_number: int, balance: int,
                 date_created: date, mangement_fee: float):
        """
        attributes: Management_fee(float)
        """
 
        super().__init__(account_number, client_number, balance, date_created)
       
        try:
            self.__management_fee = float(mangement_fee)
        except(ValueError):
            self.__management_fee = 2.55

            self._observer = ManagementFeeStrategy(date_created, date)
           
    @property
    def management_fee(self):
        """
        this will return the management fee
        """
        return self.__management_fee
   
    def __str__(self) -> str:
        """
        this will return the str
        """
        if self._BankAccount__date_created >= self.TEN_YEARS_AGO:
            management_fee = f"${self.__management_fee:.2f}"
        else:
            management_fee = "Waived"
           
        return (f"{super().__str__()}\n"
               f"Management Fee: {management_fee} Account Type: Investment")
       
       
    def get_service_charges(self) -> float:
        """
        this is  a def for getting service charges
        """
        return self._observer.calculate_service_charges(self)