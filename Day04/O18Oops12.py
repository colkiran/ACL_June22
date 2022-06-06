

class Employee:

    def __init__(self, name):
        self.__name = name                  # private variable
        self.tech = ['C#', 'asp.net', 'VB.net', 'C', 'C++', 'AngularJS', 'ReactJS']

    def __str__(self):
        return f"Name is {self.__name}\nTechnologies are :" + ", ".join(tech for tech in self.tech)


emp1 = Employee('Smith')
print(emp1)
print("-" * 40)

print(emp1.__dict__)
print("-" * 40)

emp1._Employee__name = "Will " + emp1._Employee__name
print("-" * 40)

print("Name :", emp1._Employee__name)