
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Ctor.....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print("factory.....")
        return cls(f"Mr. {fname} {lname}", age)         # call the constructor

ply1 = Player("Virat", 28)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Rohit", "Sharma", 26)
ply2.get_details()


