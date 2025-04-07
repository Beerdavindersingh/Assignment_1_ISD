__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Beerdavinder Singh"
 
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import Chequingaccount
from bank_account.savings_account import SavingAccount
from bank_account.investment_account import InvestmentAccount
from client.client import client
import os
import sys
import csv
from datetime import datetime
import logging
 
 
# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure
 
# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************
 
def load_data() -> tuple[dict, dict]:
    """
    Populates a client dictionary and an account dictionary with
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    client_listing = {}
    accounts = {}
 
    # READ CLIENT DATA
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for record in reader:
            try:
                # Extract and validate client data
                client_number = int(record['client_number'])
                first_name = record['first_name'].strip()
                last_name = record['last_name'].strip()
                email_address = record['email_address'].strip()
 
                # Check for required fields
                if not first_name or not last_name or not email_address:
                    raise ValueError("First Name, Last Name, and Email cannot be blank.")
 
                # Create and add Client object
                client_listing[client_number] = client(
                    client_number, first_name, last_name, email_address
                )
            except Exception as e:
                logging.error(f"Unable to create client: {e}")
 
    # READ ACCOUNT DATA
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for record in reader:
            try:
                # Extract and validate account data
                account_number = int(record['account_number'])
                client_number = int(record['client_number'])
                balance = float(record['balance'])
                date_created = datetime.strptime(record['date_created'], '%Y-%m-%d').date()
                account_type = record['account_type'].strip()
 
                # Additional attributes (may be null in CSV)
                overdraft_limit = (
                    float(record['overdraft_limit']) if record['overdraft_limit'] != "Null" else None
                )
                overdraft_rate = (
                    float(record['overdraft_rate']) if record['overdraft_rate'] != "Null" else None
                )
                minimum_balance = (
                    float(record['minimum_balance']) if record['minimum_balance'] != "Null" else None
                )
                management_fee = (
                    float(record['management_fee']) if record['management_fee'] != "Null" else None
                )
 
                # Determine account type and create corresponding object
                if account_type == "ChequingAccount":
                    account = Chequingaccount(
                        account_number, client_number, balance, date_created,
                        overdraft_limit, overdraft_rate
                    )
                elif account_type == "SavingsAccount":
                    account = SavingAccount(
                        account_number, client_number, balance, date_created,
                        minimum_balance
                    )
                elif account_type == "InvestmentAccount":
                    account = InvestmentAccount(
                        account_number, client_number, balance, date_created,
                        management_fee
                    )
                else:
                    logging.error(f"Not a valid account type: {account_type}")
                    continue
 
                # Validate client number exists
                if client_number in client_listing:
                    accounts[account_number] = account
                else:
                    logging.error(
                        f"Bank Account: {account_number} contains invalid Client Number: {client_number}"
                    )
            except Exception as e:
                logging.error(f"Unable to create bank account: {e}")
 
    # RETURN STATEMENT
    return client_listing, accounts
 
 
def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []
 
    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
       
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)
 
    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)
 
 
# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients, accounts = load_data()
 
    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")