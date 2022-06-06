
class Player:               # pascal casing

    def get_runs(self):     # self is like this pointer
        print(self.__class__)
        print("runs scored.....")


sachin = Player()
sachin.get_runs()

print("-" * 40)
print(type(sachin))
print(sachin.__class__)

print("-" * 40)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))           # object is the base class of all classes in python
print(isinstance(sachin, str))
