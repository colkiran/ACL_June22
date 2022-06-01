
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4.2, 5.6, 6.1, "seven", 'eight', 'nine', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
print(f"l1[0] :{l1[0]}")
l1[2] = 33
print(f"l1 :{l1}")
# l1[5] = 66
# print(f"l1 :{l1}")

print("-" * 40)
print(f"l1 :{l1}")
del l1[2]
print(f"l1 :{l1}")

print("-" * 40)
values = list(range(10, 40, 10))
print(f"values :{values}")

# unpack list
a, b, c = values
print(a, b, c, sep=",")

values = list(range(10, 101, 10))
print(f"values :{values}")
a, b, *c = values
print(a, b, c,  sep=",")

a, *b, c = values
print(a, b, c, sep=",")

*a, b, c = values
print(a, b, c, sep=",")

print("-" * 40)
l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]

print(f"l1 :{l1}")
print(f"l2 :{l2}")
print("-" * 40)

l3 = [l1, l2]
print(f"l3 :{l3}")
print("-" * 40)

l4 = [*l1, *l2]             # upack the list => remove the brackets across the list
print(f"l4 :{l4}")
