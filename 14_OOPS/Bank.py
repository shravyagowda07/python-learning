class BankAccount:
    def __init__(self,initial_balance,):
        self.balance = initial_balance
    def show_balance(self):
        print(f"Current Balance: {self.balance}")
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposite : {amount}")
            print(f"New Balance :{self.balance}")
        else:
            print("Deposite amount must be positive")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdraw : {amount}")
            print(f"New Balance : {self.balance}")
account = BankAccount(5000)
account.show_balance()
account.deposite(1000)
