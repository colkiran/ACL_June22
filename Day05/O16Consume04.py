
import gurgaon.mymodule as m
from gurgaon.mymodule import Player

m.greet("Rohit Sharma")

print("-" * 40)
ply1 = Player("Kapil Dev", 65)
ply1.get_details()

print("#" * 40)
print("#" * 40)

import sys
for pth in sys.path:
    print(pth)
