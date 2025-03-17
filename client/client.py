"""
Description: A class to manage client.py
"""
_author_ = "Beerdavinder Singh"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

class client(Observer):
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
        
        if not first_name.strip():
            raise ValueError("First name is empty") 
        
        if not last_name.strip():
            raise ValueError("Last name is empty")
        
        try:
            validate_email(email_address)
            self._email_address = email_address
        except EmailNotValidError:
            self._email_address = "beerdavinder@pixel.com"

        self._first_name = first_name
        self._last_name = last_name

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
    
    def __str__(self):
        """
        this def will print the message in a format
        """
        return f"{self.last_name}, {self.first_name} [{self.client_number}] - {self.emial_address}"
    
    def update(self, message: str) -> None:
        """
        Handles the update notification received from the subject.
        Sends an email alert with the provided message.
        """
        time = datetime.now().strftime("%Y-%M-%d %H:%M:%S")

        subject = f"Alert: unusual activty:{time}"

        email_message = f"Notification for {self._client_number}: {self._first_name} {self._last_name}: {message}"

        simulate_send_email(self._email_address, subject, email_message)


