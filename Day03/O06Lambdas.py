
def add(x, y):
    return x + y

res = add(30, 45)
print(res)

print("-" * 40)
a = add
res = a(50, 85)
print(res)

print("#" * 40)

b = lambda x, y: x + y
res = b(20, 80)
print(res)

# lambdas can be best implemented in association with three other functions
#     a. map
#     b. filter
#     c. reduce

# map
l = list(range(1, 11))
print(f"l :{l}")

res = list(map(lambda x: x ** 2, l))
print(f"res :{res}")

print("-" * 40)
temp = [25, 30, 18, 12, 36, 40, 48, 27, 20]
res1 = list(map(lambda x: (x * 9/5) + 32, temp))
print(f"res1: {res1}")

print("-" * 40)
from calendar import month_name
months = ['aug', 'apr', 'dec', 'oct', 'mar', 'nov', 'jan', 'may', 'jul', 'feb', 'jun', 'sep']
print(f"months :{months}")
sortedMonths = sorted(months, key= list(map(lambda x: x.lower()[0:3], list(month_name))).index)
print(f"sortedMonths :{sortedMonths}")

print("-" * 40)
# filter -> expression in lambda should return a True or a False
l = list(range(1, 26))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("-" * 40)
from functools import reduce
l = [8, 3, 5, 9, 4, 10, 2, 7, 11]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

res1 = reduce(lambda x, y: x + y, l)
print(f"res1 :{res1}")






