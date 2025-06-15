class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = float(initial_balance)  # =0

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount: }")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount: }")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

#creating object
operation = BankAccount(100)
operation.display_balance()
operation.deposit(67)        
operation.display_balance()
operation.withdraw(50)
operation.display_balance()
operation.withdraw(118)
operation.display_balance()
        