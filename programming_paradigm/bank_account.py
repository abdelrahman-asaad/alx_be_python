class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.2f}")
    def withdraw(self, amount):
        if self.account_balance < amount:
            print("Insufficient funds.")
        else: 
            self.account_balance -= amount   
            print(f"Withdrew: ${amount:.2f}")
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

#creating object
acc = BankAccount(100)
acc.deposit(67.0)              # ➜ Deposited: $67.0
acc.withdraw(50.0)             # ➜ Withdrew: $50.0
acc.withdraw(200.0)            # ➜ Insufficient funds.
acc.display_balance() 


        