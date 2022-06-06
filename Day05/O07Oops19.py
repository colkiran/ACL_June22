
class Animal:
    def __init__(self):
        self.a = 10
        print("Animal Ctor.....")

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print('fun method of Animal Class.....')

class Person:
    def __init__(self):
        self.p = 20
        print("Person Ctor......")

    def talk(self):
        print("Person Talks........")

    def fun(self):
        print("fun method of Person class.....")

class Girl(Animal, Person):
    def __init__(self):
        super().__init__()
        Person.__init__(self)
        self.g = 30
        print("Girl Ctor.......")


lucy = Girl()
lucy.eat()
lucy.talk()
lucy.fun()

print("-" * 40)
print(lucy.__dict__)