class Player:

    def __init__(self):         # constructor  double underscore init => dunder-init
        print("Player initialized......")

    def get_runs(self):
        print("Runs scored......")

sachin = Player()               # calls the constructor
rahul = Player()
sachin.__init__()
print("-" * 40)

sachin.get_runs()
rahul.get_runs()
