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
operation = BankAccount(100)
operation.display_balance()
operation.deposit(50)        
operation.display_balance()
operation.withdraw(20)
operation.display_balance()
operation.withdraw(140)
operation.display_balance()



        