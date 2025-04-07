__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Beerdavinder Singh"
 
from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy
 
 
class AccountDetailsWindow(DetailsWindow):
    """
    Extends the DetailsWindow class to manage account details and transactions.
    """
 
    # Signal to notify when the balance is updated
    balance_updated = Signal(BankAccount)
 
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes the AccountDetailsWindow.
        Args:
            account: The bank account to be displayed.
        """
        super().__init__()
 
        # Validate the account parameter
        if isinstance(account, BankAccount):
            # Copy the account instance to avoid modifying the original
            self.account = copy.copy(account)
 
            # Populate labels with account details
            self.account_number_label.setText(f"Account Number: {self.account.account_number}")
            self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")
 
            # Connect buttons to methods
            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)
        else:
            # Show an error message and close the dialog if account is invalid
            QMessageBox.critical(self, "Error", "Invalid account type provided.")
            self.reject()
 
    def on_apply_transaction(self):
        """
        Handles deposit and withdrawal actions.
        """
        try:
            # Attempt to convert the transaction amount to a float
            amount = float(self.transaction_amount_edit.text().strip())
            if amount <= 0:
                raise ValueError("Transaction amount must be greater than zero.")
        except ValueError as e:
            # Display error message if conversion fails
            QMessageBox.critical(self, "Transaction Failed", "Invalid transaction amount.")
            self.transaction_amount_edit.setFocus()
            return
 
        try:
            # Determine the button pressed and perform the corresponding transaction
            sender = self.sender()
            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)
 
            # Update balance label with new balance
            self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")
 
            # Clear the transaction amount input and set focus back
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
 
            # Emit the signal with the updated account
            self.balance_updated.emit(self.account)
        except Exception as e:
            # Display error message for transaction failure
            QMessageBox.critical(
                self,
                "Transaction Failed",
                f"{transaction_type} Failed: {str(e)}",
            )
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
 
    def on_exit(self):
        """
        Closes the Account Details dialog.
        """
        self.close()