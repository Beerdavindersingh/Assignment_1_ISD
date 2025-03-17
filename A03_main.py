"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Beerdavinder Singh"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account.chequing_account import Chequingaccount
from bank_account.savings_account import SavingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount
from client.client import client
from datetime import date

# 2. Create a Client object with data of your choice.
client_object = client(1756, "Beeradvinder", "Singh", "beersingh@gmail.com")
 
print(f"Client Object Created: {client_object}")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account = Chequingaccount(1539, client_object.client_number, 2100.00, date.today(), -30.00, 0.5)
print(f"The chequing account has been created: {chequing_account}")

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
savings = SavingAccount(1285, client_object.client_number, 2000.00, date.today(), 300.00)
print(f"the savings account has been created: {savings} ")

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 2) to the ChequingAccount object (created in step 3a).
chequing_account.attach(client_object)

# 4b.  Attach the Client object (created in step 2) to the SavingsAccount object (created in step 3b).
savings.attach(client_object)

# 5a. Create a second Client object with data of your choice.
second_client = client(300, "Vicky", "Ruhal", "Vruhal@gmail.com")
 
print(f"the second client has been created: {second_client}")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_second = (1543, second_client.client_number, 3000.00, date.today(), 300.00)
 
print(f"the second savings account has been created:{savings_second}")

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

print("\nChequing account transactions:")
try:
    chequing_account.deposit(1659)
    print(f"Chequing Account: Deposit succeeded.")
except Exception as e:
    print(f"Chequing account deposit error: {e}.")
       
try:
    chequing_account.withdraw(400)
    print(f"Chequing Account: Withdrawl succeeded.")
except Exception as e:
    print(f"Chequing account withdrawl error: {e}.")        
   
try:
    chequing_account.withdraw(30000)
    print(f"Chequing Account: Withdrawl succeeded.")
except Exception as e:
    print(f"Chequing account withdrawl error: {e} .")      
   
   
print("\nSavings Account transactions:")
try:
    savings.deposit(3000)
    print(f"saving account: Deposit succeeded.")
except Exception as e:
    print(f"saving account deposit error: {e}.")
       
try:
    savings.withdraw(100)
    print(f"saving account: Withdrawl succeeded.")
except Exception as e:
    print(f"saving account withdrawl error: {e}.")        
   
try:
    savings.withdraw(10000)
    print(f"saving Account: Withdrawl succeeded.")
except Exception as e:
    print(f"saving account withdrawl error: {e} .")  
