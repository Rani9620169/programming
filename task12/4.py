'''Create a BankAccount class that stores an account holder's name and balance. 
Add instance methods to deposit money, withdraw money, and display the balance. 
Do not allow a withdrawal greater than the available balance.'''

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient balance for withdrawal!")
        elif amount <= 0:
            print("Error: Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")


account = BankAccount("Anjali Verma", 500.0)
account.display_balance()
account.deposit(200.0)
account.withdraw(800.0)  
account.withdraw(150.0)  