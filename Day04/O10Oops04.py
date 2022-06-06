
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized..........")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    def __del__(self):
        print ("Object Deleted Successfully.....")

ply1= Player("Sachin", 36)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 34)              # the first argument is the name of the object that called the method
ply2.get_details()

print("-" * 40)
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)
ply2.runs = 125
print("ply2 :", ply2.__dict__)
print("ply1 :", ply1.__dict__)

print("-" * 40)