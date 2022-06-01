
# remove elements from a list
# pop, remove and clear
print("-" * 40)
print("pop".center(40, "-"))

l1 = list(range(1, 11))
print(f"l1 :{l1}")
res = l1.pop(1)
res1 = l1.pop(6)
res2 = l1.pop()             # removes the last element from the list
print(f"res :{res}")
print(f"res1 :{res1}")
print(f"res2 :{res2}")
print(f"l1 :{l1}")

print("-" * 40)
print("{:-^40}".format("remove"))
l1 = [1, 1, 2, 1, 1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 1, 1, 1, 4]
print(f"l1 :{l1}")
res = l1.remove(2)
print(f"res :{res}")
print(f"l1 :{l1}")

print("-" * 40)
print("count".center(40, "-"))
l1 = [1, 1, 2, 1, 1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 1, 1, 1, 4]
print("1 :", l1.count(1))
print("2 :", l1.count(2))
print("3 :", l1.count(3))
print("9 :", l1.count(9))

print("-" * 40)
print("index".center(40, "-"))
l1 = [1, 2, 3, 1, 2, 1, 2, 1, 1, 3, 1, 2, 1, 1, 1, 2, 3, 1, 2]
print(f"l1 :{l1}")
print(l1.index(3))
print(l1.index(3, 4))
print(l1.index(3, 10))
# print(l1.index(5))

print("-" * 40)
print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")

l2 = l1             # shallow Copy - where its not only sharing the numbers but also its adress
print(f"l2 Before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("-" * 40)
l3 = [1, 2, 3, 4, 5]
print(f"l3 Before :{l3}")
l4 = l3.copy()          # deep copy where only the values are shared
print(f"l4 Before :{l4}")

print("-" * 40)
l4.extend([6, 7])
l4.extend([8])
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("-" * 40)
l5 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(f"l5 :{l5}")

l6 = l5.copy()
print(f"l6 Before :{l6}")
l6[4].extend([60, 70, 80])

print("-" * 40)
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("-" * 40)
from copy import deepcopy
l7 = [1, 2, 3, ['a', 'b', 'c', 'd', 'e'], 4, 5]
print(f"l7 Before :{l7}")

l8 = deepcopy(l7)
print(f"l8 Before :{l8}")

l8[3].extend(['f', 'g', 'h'])

print(f"l8 After :{l8}")
print(f"l7 After :{l7}")
