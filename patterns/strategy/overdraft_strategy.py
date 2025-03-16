from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
 
class OverdraftStrategy(ServiceChargeStrategy):
    """
    A strategy for applying service charges based on overdraft conditions.
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the overdraft strategy with a limit and rate.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
       
       
    @property
    def overdraft_limit(self) -> float:
        """
        Returns the overdraft limit.
        """
        return self.__overdraft_limit
 
    @property
    def overdraft_rate(self) -> float:
        """
        Returns the overdraft rate.
        """
        return self.__overdraft_rate            
               
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates service charges based on account balance and overdraft rules
        """
        if account.balance >= self.__overdraft_limit:
            calculate_service_charge =  ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            calculate_service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE + (self.__overdraft_limit - account.balance)  * self.__overdraft_rate
       
        return calculate_service_charge