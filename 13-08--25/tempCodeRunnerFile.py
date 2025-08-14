class Account:
    acount_no=1001
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        self.account_number=Account.acount_no
        Account.acount_no+=1
    def deposit(self,amount):
        if amount >= 500:
            self.__balance+=amount
            print(f"Deposited {amount}.New balance: ₹{self.balance}")
        else:
            print("Deposit min amount of 500")
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Insufficient balance  Available: ₹{self.balance}")
        else:
            self.__balance -= amount
            print(f"Withdraw ₹{amount} . New balance: ₹{self.balance}")
    def __str__(self):
        return f"Account No: {self.account_number}, Name: {self.name}, Balance: ₹{self.balance}"
    def getbal(self, pin):
        if pin == 1234:  
            return self.__balance
        else:
            return "Invalid PIN"
        

account1=Account("saksham",20000)
account2=Account("Manglu",90000)
# account1.deposit(2000)