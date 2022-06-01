
player_count = 11
rating = 9.7
has_won_worldcup = True
team_name = "India"
print(player_count)
print(rating)
print(team_name)

print("Module Name :", __name__)     # double underscore => dunder name

a, b, c = 1, 2.5, 'three'
print(f"a :{a}, b :{b}, c :{c}")            # interpolation
print(f"a :{type(a)}")                      # RTTI - Runtime Type Identification
print(f"b :{type(b)}")
print(f"c :{type(c)}")
print(c.capitalize())

print("-" * 40)
first_name = "Sachin"
last_name = "Tendulkar"
print("My name is " + first_name + " and I am more familiar as " + last_name)
print(f"My name is {first_name } and I am more familiar as  {last_name}")           # interpolation

a = 1
b = 1
print(a + b)
a = "hello"
b = "world"
print(a + b)
x = 10
print(f"number :{x}")
print(f"binary :{0b1010}")
print(f"binary :{0b0100}")

print("-" * 40)
team_name = "Sahara India"
print(team_name)
team_name = "Sahara 'India'"
print(team_name)
team_name = 'Sahara "India"'
print(team_name)
team_name = 'Sahara \'India\''
print(team_name)

print("I can't live without water")
print('I can\'t live without water')
