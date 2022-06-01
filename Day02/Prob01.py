
l1 = [1, 1, 2, 1, 1, 2, 3, 2, 1, 2, 1, 1 ,1, 1, 1 ,1, 1, 3, 1, 2, 1, 1, 1, 1, 4]

print(f"l1 Before :{l1}")

while True:
    try:
        l1.remove(1)
    except ValueError:
        break

print(f"l1 After {l1}")