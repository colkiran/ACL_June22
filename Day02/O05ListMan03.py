

l1 = [1, 2, 3, 4.2, 5.8, 6.4, 'seven', 'eight', 'nine']

print(f"l1 :{l1}")
print(f"l1[0] :{l1[0]}")
print(f"l1[1] :{l1[1]}")
print(f"l1[2] :{l1[2]}")

print("-" * 40)
# address of these list elements
print(f"l1[0] :{l1[0]}\t{id(l1[0])}")
print(f"l1[1] :{l1[1]}\t{id(l1[1])}")
print(f"l1[2] :{l1[2]}\t{id(l1[2])}")
print(f"l1[3] :{l1[3]}\t{id(l1[3])}")

# add elements into a list
print("{:-^40}".format("append"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12])
print(f"l1 :{l1}")
print(l1[8][1:3])

print("-" * 40)
print("extend".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.extend([6, 7, 8])
l1.extend([9, 10, 11])
print(f"l1 :{l1}")

print("-" * 40)
print("insert".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")
