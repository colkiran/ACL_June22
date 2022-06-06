
class Animal:
    cntr = 0                # class attribute

    def __init__(self):
        print("Animal Ctor....")
        self.age = 1
        Animal.cntr += 1

    def eat(self):
        print("Animals eat....")

class Bird(Animal):

    def fly(self):
        print("Birds fly......")

class Fish(Animal):

    def swim(self):
        print("Fishes swim.......")


cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 40)
dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 40)
print("Total No of objects created :", Animal.cntr)

print("-" * 40)
print(cuckoo.__dict__)
print(dolphin.__dict__)


print("-" * 40)
print(f"isinstance(cuckoo, Bird)   :{isinstance(cuckoo, Bird)}")
print(f"isinstance(cuckoo, Animal) :{isinstance(cuckoo, Animal)}")
print(f"isinstance(cuckoo, Fish))  :{isinstance(cuckoo, Fish)}")
print(f"isinstance(dolphin, Bird)   :{isinstance(dolphin, Bird)}")
print(f"isinstance(dolphin, Animal) :{isinstance(dolphin, Animal)}")
print(f"isinstance(dolphin, Fish))  :{isinstance(dolphin, Fish)}")

