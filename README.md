# BANK ACCOUNT MANAGEMENT SYSTEM

The Bank Account Management System is a Python-based application that simulates banking operations such as account creation, balance inquiry, deposits, withdrawals, fund transfers, and modifications to customer details. It follows an object-oriented approach (OOP), using a class Sbi to model a real-world banking system.

# Features
# 1.Account Creation:
Users can create an account with details like name, phone number, age, Aadhaar, address, PIN, and an initial balance.
The system automatically assigns a unique Account Number.

# 2.Balance Inquiry:
Users can check their current account balance by entering their account number and PIN.

# 3.Deposit Money:
Allows users to deposit money into their account.
Updates the balance and stores transaction details.

# 4.Withdraw Money:
Users can withdraw money from their account.
Ensures PIN authentication and sufficient balance before processing.

# 5.Fund Transfer:
Users can transfer money to another valid account within the system.
Requires the recipient's account number and IFSC code for verification.

# 6.Modify Customer Details:
Users can update their name, phone number, or address.
PIN modification is also allowed with authentication.

# 7.Transaction History (Mini Statement):
Users can view a mini statement of their last transactions.
Displays transaction type (credit/debit), amount, balance, and timestamp.

# 8.Validation Checks:
Phone number, Aadhaar, PIN, and other inputs are validated to maintain security.
Ensures PIN is 4 digits, Aadhaar is 12 digits, and phone number is 10 digits.

# Technology Stack
Programming Language: Python
Concepts Used: Object-Oriented Programming (OOP)


# Class Structure (Sbi Class)
# Attributes:
Bank_Name, Bank_Loc, Ifsc_code, Bank_Mgr, Pin_Code (Bank Details)

No_Cust (Tracks total customers)

Cust_Details (Stores customer details)

transaction_details (Stores transaction history)

# Methods:
valid_ph(), valid_aadhar(), valid_pin(), valid_pin_code() → Input validation

dis_cust_check_balance() → Check balance

dis_deposit_amt() → Deposit money

dis_withdraw_amt() → Withdraw money

dis_transfer_amt() → Transfer money

dis_modify_pin() → Change PIN

dis_modify_cust_data() → Modify customer details

dis_mini_stmt() → Print mini statement

