class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount}")

    def check_balance(self):
        print(f"{self.balance}")

if __name__ == "__main__":
    account = BankAccount("Surayyo", 10000)
    account.deposit(500)
    account.check_balance()
    account.withdraw(200)
    account.check_balance()
