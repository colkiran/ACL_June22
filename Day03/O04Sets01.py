
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 40)

s2 = {1, 2, 3, 4, 5}
print(f"s2 :{s2}")
print(type(s1))
print("-" * 40)

s3 = set(range(2, 10, 2))
print(f"s3 :{s3}")
print(type(s3))
print("-" * 40)

s4 = {1, 2, 3, 4, 5, 6.4, 7.2, 8.3, 'Nine', 'Ten', 'Eleven', True, False, 15+1j, 17+2j}
print(f"s4 :{s4}")
print("-" * 40)

# iterate
for i in s4:
    print(i, end=" ")
print()

print("-" * 40)
s5 = {1, 2}
print(f's5 :{s5}')

# add new elements
s5.add(1)
s5.add(3)
s5.add(2)
s5.add(4)

print(f"s5 :{s5}")
print("-" * 40)
s5.update([1, 2, 3])
s5.update([3, 4, 5])
s5.update([2, 3, 4])
s5.update([6, 7, 8, 9])
print(f"s5 :{s5}")

# remove elements
print("-" * 40)
s5.remove(1)
s5.remove(4)
# s5.remove(10)
print(f"s5 :{s5}")

res = s5.pop()
print(f"res :{res}")
res = s5.pop()
print(f"res :{res}")

print(f"s5 :{s5}")
print("-" * 40)

s5.discard(8)
s5.discard(10)
print(f"s5 :{s5}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric_difference B :", A ^ B)
print("B symmetric_difference A :", B.symmetric_difference(A))

print("-" * 40)
# frozenset -> immutable

a = frozenset([1, 2, 3, 4, 1, 2, 5])
print(f"a :{a}")
