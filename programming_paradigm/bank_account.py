class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = float(initial_balance)
        
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:}")
        
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")