#Encapsulation in Python
class BankAccount:
    def __init__(self,initial_balance):
        self.balance = initial_balance
    
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposite : {amount}")
        else:
            print("Invalid deposite amount")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdraw:{amount}")
        else:
            print("Invalid withdrawl amount.")
    def check_balance(self):
            print(f"Current Balance:{self.balance}")
            return self.balance

account = BankAccount(5000)
account.deposite(2000)
account.withdraw(1500)
account.check_balance()

