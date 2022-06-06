
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C#', 'asp.net', 'VB.net', 'C', 'C++', 'AngularJS', 'ReactJS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)          # self.tech.__iter__()


emp1 = Employee("Micheal", 50000)
print(emp1)

print("-" * 40)
print(len(emp1))

print("-" * 40)
print([tech for tech in emp1])
