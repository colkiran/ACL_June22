
from abc import ABC, abstractmethod

class Employee:

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):
    def doJob(self):
        print("Manager's Job.....")

class Developer(Employee):
    def doJob(self):
        print("Developers Job......")


def BankFun(emp):           # polymorphism
    print("Bank Job Started.......")
    emp.doJob()
    print("Bank Job Completed......")
    print("-" * 40)

Mike  = Manager()
Dave = Developer()

BankFun(Mike)
BankFun(Dave)

print("#" * 40)
def BankFunJobs(emps):           # polymorphism
    print("Bank Job Started.......")
    for emp in emps:
        emp.doJob()
    print("Bank Job Completed......")
    print("-" * 40)

BankFunJobs([Mike, Dave])
