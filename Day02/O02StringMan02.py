
emp = "EMP-001, Jack, 38, Finance, MGR, 125000"
print(f"emp :{emp}")

print("-" * 40)
# coverting the string into a list
empLst = emp.split(", ")
print(f"empLst :{empLst}")
print(f"Emp_Name :{empLst[1]}")
desig = emp.split(", ")[4]
print(f"Designation :{desig}")
print(f"type(empLst) :{type(empLst)}")

print("-" * 40)
# convert the list back into a string
res = ", ".join(empLst)
print(f"res :{res}")
print(type(res))

print("-" * 40)
st = "the quick brown fox jumps over the lazy dog."
print(f"st :{st}")

res = st.replace('fox', "tiger")
print(f"res :{res}")

res = st.replace("the", "The", 1)
print(f"res :{res}")

print("-" * 40)
# maketrans, translate
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"
res = st.maketrans(a, b)
print(f"res :{res}")

res1 = st.translate(res)
print(f"res1 :{res1}")

print("-" * 40)
st = "the quick brown fox jumps over the lazy dog."
print(F"st :{st}")

# find
print(st.find("fox"))
print(st.find("the"))
print(st.find("the", 5))
# print(st.find("Fox"))

print("-" * 40)
print("fox" in st)
print("tiger" in st)

print("-" * 40)
# isnumeric, isdigit, isdecimal
x = "123456"
y = "abc"
print(x.isnumeric())
print(y.isnumeric())

print("Hello World")
print(repr("Hello \nWorld"))
print(str("Hello \nWorld"))

print("-" * 40)
st = "the quick brown fox jumps over the lazy dog."
print(f"st :{st}")

print("-" * 40)
st = "*********Hello*********"
print(f"st :{st}")

# left side discard *
res1 = st.lstrip("*")
print(f"res1 :{res1}")

# right side discard *
res2 = st.rstrip("*")
print(f"res2 :{res2}")

# discard * from both sides
res3 = st.strip("*")
print(f"res3 :{res3}")