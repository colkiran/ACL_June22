
# conversions
print("conversions".center(40, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("The number is {num} {num} {num}".format(num=36))
print("The number is {num} {num:f} {num:b}".format(num = 36))
print("The number is {num:10} {num:f} {num:b}".format(num=36))              # reserve 10 spaces
print("The number is {num:5} {num:f} {num:b}".format(num=36))
print("The number is {num:5} {num:f} {num:b}".format(num=3665572238))

print("Alignment".center(40, "-"))
print("{num:10}Tendulkar".format(num=50))
print("{num:15}Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))

print("#" * 40)
print("{num:15}Tendulkar".format(num="Sachin"))
# center
print("{num:^15}Tendulkar".format(num="Sachin"))
# right
print("{num:>15}Tendulkar".format(num="Sachin"))
# left
print("{num:<15}Tendulkar".format(num="Sachin"))
# fill blank space
print("{name:-^40}".format(name="Sachin Tendulkar"))
print("{name:*<40}".format(name="Sachin Tendulkar"))
print("{name:#>40}".format(name="Sachin Tendulkar"))

print("{pi:010.3}".format(pi=pi))

print("#" * 40)
print("one googol is {}".format(10 ** 100))
print("one googol is {:,}".format(10 ** 100))

