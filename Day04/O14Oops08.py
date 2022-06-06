
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.salary}"

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Kevin", 38000)
print(emp1)

print("-" * 40)
emp2 = Employee("John", 37000)
print(emp2)

print("-" * 40)
# if emp1 == emp2:
if emp1 != emp2:
    print("emp1 {0} salary of {1} is NOT equal to emp2 {2} salary of {3}".format(emp1.name, emp1.salary,
                                                                    emp2.name, emp2.salary))
else:
    print("emp1 {0} salary of {1} is equal to emp2 {2} salary of {3}".format(emp1.name, emp1.salary,
                                                                    emp2.name, emp2.salary))


print("-" * 40)
# if emp1 > emp2:
if emp1 < emp2:
    print("emp1 {0} salary of {1} is LESS than emp2 {2} salary of {3}".format(emp1.name, emp1.salary,
                                                                                 emp2.name, emp2.salary))
else:
    print("emp1 {0} salary of {1} is GREATER than emp2 {2} salary of {3}".format(emp1.name, emp1.salary,
                                                                                 emp2.name, emp2.salary))
