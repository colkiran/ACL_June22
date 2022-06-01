
"""
sort    -   sort will sort the original list
sorted  -   take a copy of the list sort it and return it
"""


l1 = [10, 3, 9, 6, 1, 4, 8, 5, 2, 7]
print(f"l1 :{l1}")

# sort the list
res1 = sorted(l1)
print(f"res1 :{res1}")

print("-" * 40)
l1 = [10, 'zebra', 'apple', 3, 'yellow', 'blue', 9, 'x_mas', 'dog', 6, 'pink', 'mango',
      1,'orange', 'red', 4, 'violet', 'green', 8, 'neon', 'cat', 5, 2, 7, 19, 151, 1276,
      27, 203, 2903, 38, 315, 3015]

print(F"l1 :{l1}")

print("-" * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 40)
cities = ['kanyakumari', 'delhi', 'thiruvananthapuram', 'bangalore', 'chennai', 'mysore',
          'vishakapatnam', 'hyderabad', 'pune', 'ooty', 'mumbai', 'coimbatore', 'kolkotta']

print(f"cities :{cities}")

print("-" * 40)
# sort the cities based on its length
res = sorted(cities, key=len)
print(f"res :{res}")

print("-" * 40)
month = ['aug', 'apr', 'dec', 'oct', 'mar', 'nov', 'jan', 'may', 'jul', 'feb', 'jun', 'sep']
print(f"month :{month}")

# sort the months according to the claendar
from calendar import month_name

def sortMonth(mnt):
    months = []
    for m in list(month_name):
        months.append(m[0:3].lower())
    if mnt in months:
        return months.index(mnt)

print(f"month :{month}")
res = sorted(month, key=sortMonth)
print(f"Sorted Months :{res}")

print("-" * 40)
print("clear".center(40, "-"))

l = list(range(1, 11))
print(f"l :{l}")

l.clear()
print(f"l :{l}")





