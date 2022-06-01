
# emulate printf of C language
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "superb")           # tuples
print(values)

print(format % values)
print("-" * 40)

format = "Welcome %s, your rating of %.3f, what a %s player"

print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.5, "class"))
print(format % ("Sachin", 4.532, "class"))
print(format % ("Sachin", 4.532556, "class"))
print(format % ("Sachin", 4.5328567, "class"))

print("-" * 40)
# emulate unix shell syntax
from string import Template
tmpl = Template("Welcome $name, What a $adjective player")
print(tmpl)
print(tmpl.substitute(name="Sachin", adjective="class"))
print("-" * 40)

# format strings from python

print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {2}, what a {0} player for {1}".format( "class", "India","Sachin"))
print("Welcome {plyr}, what a {adj} player for {cntry}".format( adj = "class", cntry = "India", plyr = "Sachin"))
print("Welcome {name} your rating  of {rating} what a player".format(name= "Sachin", rating=4.3))

# interpolation
from math import pi, e
print("PI :{} and Eulers Constant :{}".format(pi, e))
print("PT {} and Eulers Constant {} magic number {magic} ".format(pi, e, magic=40585))
print("PI = {0}, eulers constant {1} and magic number {magic}".format(pi, e, magic=40585))

print("-" * 40)
full_name = ["Sachin", "Tendulkar"]
print('Mr. {name}'.format(name=full_name))
print("Mr. {name[0]}".format(name=full_name))
print("Mr. {name[1]}".format(name=full_name))
print("Mr. {name[0]} {name[1]}".format(name=full_name))

import math
print("The {mod.__name__} module gives the value of pi = {mod.pi} and eulers e = {mod.e}".format(mod=math))
