
st = "Hello World"
print(f"st :{st}")

# strings strored in python
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

# extract a part of a string (slicing)
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")
print(f"st[0:11:1] :{st[0:11:1]}")              # 1 - increment value
print(f"st[0:11:2] :{st[0:11:2]}")
print(f"st[10::-1] :{st[10::-1]}")

# reverse Indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

# reverse slicing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 40)
# strings are immutable
print(f"st[6] :{st[6]}")
# st[6] = "w"

print("-" * 40)
print(dir(st))
