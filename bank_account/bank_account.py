from datetime import date
from patterns.observer.subject import subject
from patterns.observer.observer import Observer
from abc import ABC

class BankAccount(subject, ABC):
    LARGE_TRANSACTION_THRESHOLD : float = 9999.99
    LOW_BALANCE_LEVEL : float = 50.0
    """
    A Class for Bank Account
    """

    def __init__(self, account_number:int, client_number: int, balance: float, date_created: date):
        """
        Attributes:
            AccountNumber(int)
            ClientNumber(int)
            Balance(float)
        """
        super().__init__()

        if isinstance(account_number, int):
            self._account_number = account_number
        else:
            raise ValueError("Account number must be an integar")
        
        if isinstance(client_number,int):
            self._client_number = client_number
        else:
            raise ValueError("Client number must be an integar.")
        
        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

        if isinstance(date_created, date):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()


    @property 
    def account_number(self) -> int:
        """
        this def will return the value of the account number
        """
        return self._account_number
    
    @property
    def client_number(self) -> int:
        """
        this def will return the value of the client number
        """
        return self._client_number
    
    @property
    def balance(self) -> float:
        """
        this def returns the balance of the account
        """
        return self._balance

    @property
    def date_created(self) -> date:
        """
        
        """
        return self.__date_created    
       
    def update_balance(self,amount:float):
        """
        this def will update the balance according to the transaction
        """
        try:
            amount = float(amount)
            self._balance += amount
        except ValueError: 
            print("Balance is not updated")

    def deposit(self, amount:float):
        """
        This def will deposit the amount
        but will raise a error if the deposit is not in numeric value
        and also if the deposit is not a positive value
        """
        if not isinstance(amount, (int,float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <=0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Deposit amount: {formatted_amount} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self,amount:float):
        """
        this def will withdraw the amount  from the account or will
        raise a error if the withdraw amount is not a numeric value
        or if the withdraw amount is not positive
        or if the withdraw amount exceeds the amount of balance in the account
        """
        if not isinstance(amount, (int,float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric. ")
        
        if amount <=0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Withdrawal amount: {formatted_amount} must be positive.")
        
        if amount > self._balance:
            formatted_balance = f"${self._balance:,.2f}"
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Withdrawal amount: {formatted_amount} must not exceed the account balance: {formatted_balance}")
        
        self.update_balance(-amount)

    def __str__(self):
        """
        this def will print the result in the format
        """
        formatted_balance = f"${self._balance}"
        return f"Account number: {self._account_number} Balance: {formatted_balance}"

    def get_service_charges(self) -> float:
        """
        
        """
        return self.BASE_SERVICE_CHARGE
    
    def attach(self, observer: Observer) -> None:
        """
        Adds an observer to the subject.

        Args:
           observer (Observer): The observer to add.
        """
        if observer in self.__observer:
            self.__observer.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the subject.

        Args:
           observer (Observer): The observer to remove.
        """
        if observer in self.__observer:
            self.__observer.remove(observer)

    def notify(self, message: str) -> None:
        """
        Sends a message to all observers.

        Args:
           message (str): The message to send.
        """
        for observer in self.__observer:
            observer.update(message)



    
