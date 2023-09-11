# Problem Statement #
# Implement a basic structure of a parent class, Account, and a child class, SavingsAccount.
# Task 1 # Implement properties as instance variables and set them to None or 0.
# Account has the following properties:
#     title
#     balance
# SavingsAccount has the following properties:
#     interestRate
# Task 2 # Create an initializer for Account class. The order of parameters should be the following:
# Account("Ashish", 5000)
# where Mark is the title and 5000 is the account balance.
# Task 3 # Implement properties as instance variables and set them to None or 0.
# Create an initializer for SavingsAccount class using the initializer of the Account class in the order below:
# Account("Ashish", 5000, 5)
#paent class
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
account = Account("Ashish", 5000)
savings_account = SavingsAccount("Ashish", 5000, 5)
print("Account Title:", account.title)
print("Account Balance:", account.balance)
print("Savings Account Title:", savings_account.title)
print("Savings Account Balance:", savings_account.balance)
print("Savings Account Interest Rate:", savings_account.interestRate)
