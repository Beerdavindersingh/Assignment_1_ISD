__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Beerdavinder Singh"
 
from PySide6.QtWidgets import (QLineEdit, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QMessageBox, QPushButton, QLabel, QWidget)
from PySide6.QtCore import Qt, Slot
from user_interface.manage_data import load_data, update_data
from user_interface.account_details_window import AccountDetailsWindow
from bank_account.bank_account import BankAccount
 
 
class ClientLookupWindow(QWidget):
    def __init__(self):
        """
        Initializes the ClientLookupWindow.
        """
        super().__init__()
 
        # Explicitly set up layout and widgets
        self.layout = QVBoxLayout(self)
 
        # Initialize and set up widgets
        self.client_number_edit = QLineEdit(self)
        self.client_number_edit.setPlaceholderText("Enter Client Number")
        self.client_number_edit.setText("")  # Clear any pre-set values
        self.layout.addWidget(QLabel("Client Lookup", self))
        self.layout.addWidget(self.client_number_edit)
 
        self.lookup_button = QPushButton("Lookup Client", self)
        self.layout.addWidget(self.lookup_button)
 
        self.client_info_label = QLabel("", self)
        self.layout.addWidget(self.client_info_label)
 
        # Initialize account_table as QTableWidget
        self.account_table = QTableWidget(self)
        self.account_table.setColumnCount(4)
        self.account_table.setHorizontalHeaderLabels(
            ["Account Number", "Balance", "Date Created", "Account Type"]
        )
        self.layout.addWidget(self.account_table)
 
        # Load data
        self.client_listing, self.accounts = load_data()
        print(f"DEBUG: Clients Loaded: {len(self.client_listing)} clients.")
        print(f"DEBUG: Accounts Loaded: {len(self.accounts)} accounts.")
 
        # Connect signals to slots
        self.lookup_button.clicked.connect(self.on_lookup_client)
        print("DEBUG: lookup_button signal connected.")
 
        self.account_table.cellClicked.connect(self.on_select_account)
 
    @Slot()
    def on_lookup_client(self):
        """
        Handles the event when the lookup button is clicked.
        """
        # Clear previous display
        self.reset_display()
 
        # Get input from the client_number_edit field
        client_number_input = self.client_number_edit.text().strip()
 
        # Debugging: Check what input was captured
        print(f"DEBUG: client_number_edit text = '{self.client_number_edit.text()}'")
        print(f"DEBUG: client_number_edit stripped text = '{client_number_input}'")
 
        # Validate input is not empty
        if not client_number_input:
            QMessageBox.critical(self, "Input Error", "Client number field cannot be empty.")
            return
 
        # Validate input is numeric
        try:
            client_number = int(client_number_input)
        except ValueError:
            QMessageBox.critical(self, "Non-Numeric Client", "The client number must be a numeric value.")
            return
 
        # Debugging: Verify client_number after conversion
        print(f"DEBUG: Converted Client Number = {client_number}")
 
        # Check if the client exists in the client_listing dictionary
        if client_number not in self.client_listing:
            print(f"DEBUG: Client {client_number} not found. Available clients: {list(self.client_listing.keys())}")
            QMessageBox.warning(self, "Client Not Found", f"Client number: {client_number} not found.")
            return
 
        # Retrieve and display client details
        client = self.client_listing[client_number]
        self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")
 
        # Populate the account table with the client's accounts
        self.account_table.setRowCount(0)
        for account in self.accounts.values():
            if account.client_number == client_number:
                print(f"DEBUG: Adding Account {account.account_number} for Client {client_number}")
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)
 
                # Populate table columns
                self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account.account_number)))
                self.account_table.setItem(row_position, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                self.account_table.setItem(row_position, 2, QTableWidgetItem(account.date_created.strftime('%Y-%m-%d')))
                self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))
 
                # Align text in cells
                for col in range(4):
                    self.account_table.item(row_position, col).setTextAlignment(Qt.AlignCenter)
 
        # Resize columns to fit content
        self.account_table.resizeColumnsToContents()
 
    def reset_display(self):
        """
        Resets the display for new lookup data.
        """
        self.client_info_label.setText("")
        self.account_table.setRowCount(0)
 
    def update_data(self, account: BankAccount):
        """
        Updates the account table and accounts dictionary with the new balance.
        Args:
            account: The updated BankAccount object.
        """
        for row in range(self.account_table.rowCount()):
            # Compare account number with the first column of the table
            table_account_number = int(self.account_table.item(row, 0).text())
            if table_account_number == account.account_number:
                # Update balance column
                self.account_table.setItem(row, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
 
                # Update accounts dictionary
                self.accounts[account.account_number] = account
 
                # Update the CSV file
                update_data(account)
 
                break
 
    @Slot(int, int)
    def on_select_account(self, row: int, column: int) -> None:
        """
        Handles the event when a cell in the account table is clicked.
        Opens the Account Details window for the selected account.
        """
        # Obtain the account number from the selected row
        account_number_item = self.account_table.item(row, 0)
 
        if not account_number_item or not account_number_item.text().strip():
            # Display an error if the account number is null
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid account.")
            return
 
        try:
            # Convert the account number to an integer
            account_number = int(account_number_item.text().strip())
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid account number format.")
            return
 
        # Check if the account exists in the accounts dictionary
        if account_number not in self.accounts:
            QMessageBox.critical(self, "Bank Account Does Not Exist", f"Account number: {account_number} does not exist.")
            return
 
        # Retrieve the BankAccount object for the selected account
        account = self.accounts[account_number]
 
        # Debugging: Print the selected account details
        print(f"DEBUG: Selected Account Details - {account}")
 
        # Create an instance of AccountDetailsWindow and pass the account
        account_details_window = AccountDetailsWindow(account)
 
        # Connect the signal to update_data
        account_details_window.balance_updated.connect(self.update_data)
 
        account_details_window.exec_()