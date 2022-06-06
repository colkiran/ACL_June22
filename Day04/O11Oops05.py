
class Player:
    # class attribute or class variable
    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 34)
ply1.get_details()

print("-" * 40)
ply2 = Player('Sourav', 31)
ply2.get_details()

print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
ply2.team = "KKR"
print(f"ply2 :{ply2.team}")
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")

print("-" * 40)
print("ply2 :", ply2.__dict__)              # class attribute's value cannot be changed using an object

