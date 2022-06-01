
"""
int
float
complex
"""

a = 10
b = -10

print(f"a :{a}")
print(f"a :{type(a)}")
print(f"b :{b}")
print(f"b :{type(b)}")

print("-" *  40)
c = 10.0
d = -10.0

print(f"c :{c}")
print(f"c :{type(c)}")
print(f"d :{d}")
print(f"d :{type(d)}")

print("-" *  40)
e = +2e3
f = -2e3
print(f"e :{e}")
print(f"e :{type(e)}")
print(f"f :{f}")
print(f"f :{type(f)}")

print("-" *  40)
g = 8.69J
h = -8.69J
print(f"g :{g}")
print(f"g :{type(g)}")
print(f"h :{h}")
print(f"h :{type(h)}")

print("-" *  40)
# how to print a number in exponential format
x = float(2500000)
print(f"x :{x}")
print(format(x, '.1E'))

print("-" *  40)
x = 1
y = 2.5
z = x + y
print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("conversion".center(50, "-"))
a = -100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(40, "-"))
print(11)       # decimal
print(0b11)     # binary
print(0b101)    # binary
print(0o11)     # octal
print(0o111)    # octal
print(0xe)      # hexa
print(0xa)      # hexa

print("Number System Conversion".center(50, "-"))
a = 100
print(f"a :{a}")
print("Octal :", oct(a))
print("Hexa :", hex(a))
print("Bin :", bin(a))
