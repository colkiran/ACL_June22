
import sys

sys.path.append("C:/Delhi")

for path in sys.path:
    print(path)

import gurgaon.mymodule as m
m.greet("Sachin")

from gurgaon.mymodule import Player
ply1 =Player("Micheal Jordan", 56)
ply1.get_details()
