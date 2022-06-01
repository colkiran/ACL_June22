
player = {'name': 'Sachin', 'runs': 145, 'oppn': 'West Indies', 'venue': 'Sabina Park'}
print(f"player :{player}")
print(type(player))

print("-" * 40)
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('runs', 85), ('oppn', 'sri lanka'), ('venue', 'chepauk')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(prod="Dairy Milk", category="choclate", price=170, qty=2)
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# create
player = {'name': 'Sachin', 'runs': 145, 'oppn': 'West Indies', 'venue': 'Sabina Park'}
print(f"player :{player}")
print(type(player))

# read
print(f"Player Name :{player['name']}")
print(f"Opponent :{player['oppn']}")

# update / add new
print(f"player :{player}")
player['year'] = 2003           # New Key - Add it
player['runs'] = 165            # Key already existing - Modify the data
print(f"player :{player}")

# delete
del player['year']
del player['runs']
print(f"player :{player}")

print("-" * 40)
player = {'name': 'Sachin', 'runs': 145, 'oppn': 'West Indies', 'venue': 'Sabina Park', 'year': 2003}
# iterate on the dictionary
for x in player:
    # print(x, end=" ")
    print(x, "=>", player[x])
print()

print("-" * 40)
# print(player['age'])
print(player.get('age'))                # none
print(player.get('oppn'))               # WI

print("-" * 40)
print(dir(player))
