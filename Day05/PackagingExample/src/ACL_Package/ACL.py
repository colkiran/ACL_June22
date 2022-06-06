
gname = "Rahul Dravid"

runs = {'test': 16500, 'odi': 18000, 't20': 580}

sports = ['cricket', 'tennis', 'hockey', 'soccer', 'swimming']

def greet(gst):
    print(f"Greetings {gst}, Welcome to the event")


class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"The name of the player is :{self.name}")
        print(f"The age of the player is :{self.age}")


        