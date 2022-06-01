
"""
1. arithmetic
2. comparison or relational
3. logical
4. Bitwise
5. ternary
"""

print("Arithmetic Operators".center(40, "-"))
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)      # floor division - integer result

print("-" *  40)
print(10 % 3)       # modulus
print(10 ** 3)

print("Augmentor".center(40, "-"))
# =, +=(++), -=, *=, /=
x = 10
print(f"x :{x}")
x += 5
print(f"x :{x}")
print("-" *  40)
x //= 3
print(f"x :{x}")
print("-" *  40)
x *= 5
print(f"x :{x}")
x %= 3
print(f"x :{x}")

print("comparison".center(40, "-"))
# ==, >, <, >=, <=, !=
x = 10
y = 8
print(x == y)
print(x >= y)
print(x <= y)
print(x != y)

print("Logical Operator".center(40, "-"))
print(1 == 1 and 2 == 2)
print(1 == 1 and 1 == 2)
print("-" *  40)

print(1 == 1 or 2 == 2)
print(1 == 2 or 2 == 2)
print(1 == 1 or 2 == 1)
print("-" *  40)

print(not(1 == 1 and  2 == 2))
print(not(1 == 1 or 1 == 2))

print("-" *  40)
print("ASCII".center(40, "-"))
print(f"a :{ord('a')}\tA :{ord('A')}")
print(f"z :{ord('z')}\tZ :{ord('Z')}")

print("apple" > "orange")
print("orange" > "apple")

print("Bitwise Operators".center(40, "-"))
print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)
print(5 << 2)
print(16 >> 1)
print(5 >> 1)

print(~0)           #(0000 => 1111 =>  -1 )
print(~5)           #(0101 => 1010 =>  -6 )

print("Ternary Operator".center(40, "-"))
age = 20
print("Can Vote" if age >= 18 else "Cannot Vote")
