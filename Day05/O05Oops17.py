
class Animal:
    def __init__(self):
        print("Animal Ctor.....")
        self.age = 1

    def Eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def __init__(self):
        super().__init__()                  # calls the parent class constructor
        self.weight = '1.5 kg'
        print("Bird Ctor.....")

    def Fly(self):
        print("Birds Fly.....")

cuckoo = Bird()
cuckoo.Eat()
cuckoo.Fly()
print("-" * 40)

print(cuckoo.__dict__)
