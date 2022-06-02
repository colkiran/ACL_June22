
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3
print(f"t5 :{t5}")
print(type(t5))

print("-" * 40)
t1 = (1, 2, 3, 4.2, 5.9, 6.4, 'seven', 'eight', 'nine', True, False )
print(F"t1 :{t1}")
print(f"t1[6] :{t1[6]}")
print(f"t1[6:10] :{t1[6:10]}")

print("-" * 40)
print(t1[6])
# t1[6] = "SEVEN"

t10 = (1, 2, 3, [4, 5, 6, 7], 5)
print(f"t10 :{t10}")
print(t10[3])
t10[3][2] = 'six'
print(f"t10 :{t10}")

print("-" * 40)
print(dir(t1))

t1 = (1, 2, 1, 2, 1, 2, 3, 1, 1, 2, 1, 3, 1, 2, 3, 3, 2)
print(f"t1 :{t1}")
print(f"t1.count(1) :{t1.count(1)}")

print(f"t1.index(3) :{t1.index(3)}")
print(f"t1.index(3) :{t1.index(3, 7)}")
print(f"t1.index(3) :{t1.index(3, 12)}")
