
class Animal:
    def eat(self):
        print("Animals eat.....")

class Bird(Animal):
    def fly(self):
        print("Birds fly......")

class Chicken(Bird):
    def Breed(self):
        print("Chickens are breeded to consume.....")

    def fly(self):
        print("Chickens seldom fly......")

chick = Chicken()

chick.Breed()
chick.fly()
chick.eat()

