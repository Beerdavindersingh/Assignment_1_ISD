from bank_account.bank_account import BankAccount
from bank_account.chequing_account import Chequingaccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingAccount
 
 
from datetime import date

# Step 2: Create a ChequingAccount instance with a balance below the overdraft limit
chequing = Chequingaccount(22222, 3333, -50, date.today(), 200.00, 0.05)

# Step 3: Print ChequingAccount details
print(chequing)
print(f"Service Charges: ${chequing.get_service_charges():.2f}")

# Step 4: Deposit enough to avoid overdraft fees, then print details
chequing.deposit(300)
print(chequing)
print(f"Service Charges: ${chequing.get_service_charges():.2f}")

print("===================================================")

# Step 5: Create a SavingsAccount instance with a balance above the minimum balance
savings = SavingAccount(22222, 3333, 4444.44, date.today(), 200.00)

# Step 6: Print SavingsAccount details
print(savings)
print(f"Service Charges: ${savings.get_service_charges():.2f}")

# Step 7: Withdraw enough to fall below the minimum balance, then print details
savings.withdraw(600)
print(savings)
print(f"Service Charges: ${savings.get_service_charges():.2f}")

print("===================================================")

# Step 8: Create an InvestmentAccount within the last 10 years
investment_recent = InvestmentAccount(22222, 3333, 4444.44, date(2020, 3, 10), 4.00)

# Step 9: Print InvestmentAccount details
print(investment_recent)
print(f"Service Charges: ${investment_recent.get_service_charges():.2f}")

# Step 10: Create an InvestmentAccount older than 10 years
investment_old = InvestmentAccount(404, 50, 7000, date(2005, 3, 20), 4.00)

# Step 11: Print InvestmentAccount details
print(investment_old)
print(f"Service Charges: ${investment_old.get_service_charges():.2f}")

print("===================================================")

# Step 12: Deduct service charges from each account
accounts = [chequing, savings, investment_recent, investment_old]
for account in accounts:
    account.withdraw(account.get_service_charges())

# Step 13: Print final details of all accounts
for account in accounts:
    print(account)



