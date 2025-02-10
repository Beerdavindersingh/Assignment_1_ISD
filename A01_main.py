"""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from bank_account.bank_account import BankAccount
from client.client import client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    Client = None
    try:
        Client = client(1010, "John", "Doe", "johndoe@example.com")
        print(f"Client created: {Client}")
    except ValueError:
        print(f"Error creating client")

    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance.
    try:
        bank_account = BankAccount(20019, 1010, 1000.0)
    except ValueError:
        print(f"Error creating bank account")

    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance.
    try:
        bank_account = BankAccount(20020, 1010, "invalid_balance")
    except ValueError:
        print(f"Error creating bank account with invalid balance")

    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    print(f"Client: {client}")
    print(f"BankAccount: {bank_account}")

    # 6. Attempt to deposit a non-numeric value into the BankAccount created in step 3. 
    try:
        bank_account.deposit("non_numeric_value")
    except ValueError:
        print(f"Error during deposit")

    # 7. Attempt to deposit a negative value into the BankAccount created in step 3.
    try:
        bank_account.deposit(-100)
    except ValueError:
        print(f"Error during deposit")

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount created in step 3.
    try:
        bank_account.withdraw(200)
        print(f"BankAccount after valid withdrawal: {bank_account}")
    except ValueError:
        print(f"Error during withdrawal")

    # 9. Attempt to withdraw a non-numeric value from the BankAccount created in step 3.
    try:
        bank_account.withdraw("non_numeric_value")
    except ValueError:
        print(f"Error during withdrawal")

    # 10. Attempt to withdraw a negative value from the BankAccount created in step 3.
    try:
        bank_account.withdraw(-50)
    except ValueError:
        print(f"Error during withdrawal")

    # 11. Attempt to withdraw a value from the BankAccount created in step 3 which 
    # exceeds the current balance of the account.
    try:
        bank_account.withdraw(2000)
    except ValueError:
        print(f"Error during withdrawal")

    # 12. Code a statement which prints the BankAccount instance created in step 3.
    print(f"Final BankAccount: {bank_account}")

if __name__ == "__main__":
   main()