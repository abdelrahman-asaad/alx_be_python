class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")
    def withdraw(self, amount):
        if self.account_balance < amount:
            print("Insufficient funds.")
        else: 
            self.account_balance -= amount   
            print(f"Withdrew: ${amount:.1f}")
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.1f}")

#creating object
operation = BankAccount(100)
operation.display_balance()
operation.deposit(67)        
operation.display_balance()
operation.withdraw(50)
operation.display_balance()
operation.withdraw(118)
operation.display_balance()



        