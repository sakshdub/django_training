import random

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = self.generate_account_number()
        self.account_holder = account_holder
        self.__balance = balance

    
    def generate_account_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    def deposit(self, amount):
        if amount >= 500:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit min amount of ₹500")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insufficient balance. Available: ₹{self.__balance}")
        else:
            self.__balance -= amount
            print(f"Withdraw ₹{amount}. New balance: ₹{self.__balance}")

    def display_balance(self):
        print(f"Current balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance


class SavingAccount(BankAccount):
    interest_rate = 0.04  # 4%   by bank

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest ₹{interest}  at {self.interest_rate * 100}%")


class CurrentAccount(BankAccount):
    overdraft_limit = 50000  # ₹50,000 fixed by bank

    def withdraw(self, amount):
        if self.get_balance() - amount < -self.overdraft_limit:
            print(f"Overdraft limit exceeded! Limit: ₹{self.overdraft_limit}")
        else:
            self._BankAccount__balance = self.get_balance() - amount
            print(f"Withdraw ₹{amount}. New balance: ₹{self.get_balance()}")


# ===== Program Flow =====
account_type = input("Enter account type (saving/current): ").lower()
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

if account_type == "saving":
    acc = SavingAccount(name, balance)
    print(f"Account created. Number: {acc.account_number}")
    print(f"Interest Rate: {SavingAccount.interest_rate * 100}%")
elif account_type == "current":
    acc = CurrentAccount(name, balance)
    print(f"Account created. Number: {acc.account_number}")
    print(f"Overdraft Limit: ₹{CurrentAccount.overdraft_limit}")
else:
    print("Invalid selection")
    exit()

while True:
    print("\nChoose operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    if isinstance(acc, SavingAccount):
        print("4. Apply Interest")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        acc.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        acc.withdraw(amt)
    elif choice == "3":
        acc.display_balance()
    elif choice == "4" and isinstance(acc, SavingAccount):
        acc.apply_interest()
    elif choice == "5":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice!")
