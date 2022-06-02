
fruits = [
    ('apple', 280),
    ('orange', 140),
    ('Pine', 85),
    ('Gauva', 120),
    ('watermelon', 70),
    ('strawberry', 320),
    ('grapes', 160)
]

print(f"fruits :{fruits}")

print("-" * 40)

prices = ["fruit" for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
price = [fruit[0] for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[1] for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[1] * 0.75 for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
expFruits = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits if fruit[1] > 100]
print(f"Expensive Fruits :{expFruits}")
