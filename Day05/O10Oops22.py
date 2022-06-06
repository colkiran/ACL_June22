
# duck types

class Manager:
    def doJob(self):
        print("Managers KSRTC job.....")

class Developer:
    def doJob(self):
        print("Developers Job.......")

Mike= Manager()
Dave = Developer()

def BankFunJobs(emps):           # polymorphism
    print("Bank Job Started.......")
    for emp in emps:
        emp.doJob()
    print("Bank Job Completed......")
    print("-" * 40)

BankFunJobs([Mike, Dave])
