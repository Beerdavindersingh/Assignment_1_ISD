"""
Description: A class to manage client.py
"""
_author_ = "Beerdavinder Singh"

from email_validator import validate_email,EmailNotValidError

class client:
    """
    A client class with client_number as integar, first_name as string, last_name as string, email_address as string
    """
    def __init__(self,client_number:int, first_name:str, last_name:str,email_address:str):
        """
        Attributes:
            client_number(int)
            first_name(string)
            last_name as a (string)
            email_address as a (string)
        ValueError:
            client_number: Will raise a error if the client number is not an integar
            first_name: Will raise a error if the first name is empty
            last_name: Will raise a error if the last name is empty
            emial_address: Will raise a error if the email is not valid
        """
        if isinstance(client_number,int):
           self._client_number = client_number
        else:
            raise ValueError("Client number should be a integar to be valid") 
        
        if len(first_name.strip()) == 0:
            self._first_name = first_name.strip()
        else:
            raise ValueError("First name is empty") 
        
        if len(last_name.strip()) == 0:
            self._last_name = last_name.strip()
        else:
            raise ValueError("Last name is empty")
        
        try:
            validate_email(email_address)
            self._email_address = email_address
        except EmailNotValidError:
            self._email_address = "email@pixell-river.com"


    @property
    def client_number(self) -> int:
        """
        this def will return client number
        """
        return self._client_number
    
    @property
    def first_name(self) -> str:
        """
        this def will return first number
        """
        return self._first_name
    
    @property
    def last_name(self) -> str:
        """
        this def will return last name
        """
        return self._last_name
    
    @property 
    def emial_address(self) -> str:
        """
        this def will return the email address
        """
        return self._email_address
    
    def _str_(self):
        """
        this def will print the message in a format
        """
        return f"{self.last_name}, {self.first_name} [{self.client_number}] - {self.emial_address}"

