
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C#', 'asp.net', 'VB.net', 'C', 'C++', 'AngularJS', 'ReactJS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)          # self.tech.__iter__()

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value


emp1 = Employee("David", 85000)
print(emp1)

print("-" * 40)
print([tech for tech in emp1])

print("-" * 40)
x = emp1[3]
print(f"x :{x}")

print("-" * 40)
emp1[1] = "MVC"

print("-" * 40)
print([tech for tech in emp1])
