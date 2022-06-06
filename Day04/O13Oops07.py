
# magic methods
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

ply1 = Player("Rahul", 30)

print("-" * 40)
print(str(ply1))

print("-" * 40)
print(ply1)                 # implitcitly calls __str__