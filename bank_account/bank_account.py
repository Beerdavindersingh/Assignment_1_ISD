class BankAccount:
    """
    A Class for Bank Account
    """
    def _init_(self, account_number: int, client_number: int, balance: float):
        """
        Attributes:
            AccountNumber(int)
            ClientNumber(int)
            Balance(float)
        """
        if isinstance(account_number, int):
            self._account_number = account_number
        else:
            raise ValueError("Account number should be an integar")
        
        if isinstance(client_number,int):
            self._client_number = client_number
        else:
            raise ValueError("Client number should be an integar.")
        
        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0
