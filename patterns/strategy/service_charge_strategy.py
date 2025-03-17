from bank_account.bank_account import BankAccount
class ServiceChargeStrategy:
    """
    A strategy for calculating service charges on bank accounts.
    """
    # The base service charge amount.
    BASE_SERVICE_CHARGE:float = 0.50
    
   
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charges for the given bank account.
        """
        pass