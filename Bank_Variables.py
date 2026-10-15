'''Question 5: Global vs. Local Bank
Define a global variable bank_balance = 5000 . Write two functions: deposit(amount) and withdraw(amount) .
Inside these functions, use the global keyword to update the bank_balance using assignment operators ( += , -
= ). Ensure that a user cannot withdraw more than their current balance. Call both functions and print the updated
balance.'''

bank_balance = 5000
def deposit(amount):
    global bank_balance
    bank_balance += amount

def withdraw(amount):
    global bank_balance

    if amount <= bank_balance:
        bank_balance -= amount
    else:
        print("Not enough balance!")

deposit(500)
withdraw(1000)
print("Bank Balance:", bank_balance)
