

print("-" * 40)
print("keys".center(40, "-"))

player = {'name': 'Rahul', 'runs': 85, 'oppn': "South Africa", 'venue': 'wanderers', 'year': 2001}
print(f"player :{player}")

kys  = player.keys()
print(f"keys :{kys}")
print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))


print("-" * 40)
print("Values".center(40, "-"))
print(f"player :{player}")
player['country'] = None                # None is null in python
print(len(player))
print(f"player :{player}")

vl = player.values()
print(f"Values :{vl}")

print("-" * 40)
print("fromkeys".center(40, "-"))

# convert a list into keys of a dictionary
cities = ['blr', 'che', 'mum', 'hyd', 'del', 'kol', 'pun']
print(f"cities :{cities}")

temp1 = dict.fromkeys(cities)           # values will be None by default
print(f"temp1 :{temp1}")

temp2 = dict.fromkeys(cities, 22)
print(f"temp2 :{temp2}")

print("-" * 40)
print("setdefault".center(40, "-"))
player = {'name': 'sourav', 'team': 'india'}
print(f"player :{player}")
player.setdefault('runs', 185)
player.setdefault('team', 'KKR')
print(f"player :{player}")

print("-" * 40)
print("pop".center(40, "-"))
player = {'name': 'Rahul', 'runs': 85, 'oppn': "South Africa", 'venue': 'wanderers', 'year': 2001}
print(f"player :{player}")
res = player.pop('year')
print(f"res :{res}")
res = player.pop('oppn')
print(f"res :{res}")

# res = player.pop("year")
# print(f"res :{res}")

print(f"Player :{player}")

print("-" * 40)
print("popitem".center(40, "-"))
player = {'name': 'Rahul', 'runs': 85, 'oppn': "South Africa", 'venue': 'wanderers', 'year': 2001}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

print("-" * 40)
print("get".center(40, "-"))
player = {'name': 'Rahul', 'runs': 85, 'oppn': "South Africa", 'venue': 'wanderers', 'year': 2001}
print(f"player :{player}")

print(player.get('oppn', "Please enter a valid key...."))
print(player.get('runs', "Please enter a valid key...."))
print(player.get('age', "Please enter a valid key...."))
