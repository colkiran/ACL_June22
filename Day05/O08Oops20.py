
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account Ctor.....")

    @abstractmethod
    def getBalance(self):
        pass


class Savings(Account):
    def withdraw(self):
        print("Amount debted from the account successfully.....")

    def getBalance(self):
        print("Balance in the account is  ######.##")


class Current(Account):

    def deposit(self):
        print("Amount successfully credited into the account.......")


    def getBalance(self):
        print("Balance in the account is  ######.##")

save = Savings()
save.withdraw()
save.getBalance()

print("-" * 40)

cur = Current()
cur.deposit()
cur.getBalance()

