
emp = {
    'emp1': {'empid': 1289, 'empname': 'Kevin', 'age': 34, 'dept': 'Finance', 'desig': 'MGR', 'sal': 85000},
    'emp2': {'empid': 2801, 'empname': 'Grace', 'age': 31, 'dept': 'MKT', 'desig': 'BDM', 'sal': 45000},
    'emp3': {'empid': 3670, 'empname': 'Richards', 'age': 29, 'dept': 'IT', 'desig': 'Analyst', 'sal': 70000}
}

print(f"emp :{emp}")

print("-" * 40)
print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
# items => keys + values
for ky, info in emp.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("{:-^40}".format("update"))
emp1 = {'empid': 1289, 'empname': 'Kevin', 'age': 34, 'dept': 'Finance', 'sal': 85000}
emp2 = {'empid': 2801, 'empname': 'Grace', 'age': 31, 'desig': 'BDM', 'sal': 45000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

# update emp2's values into emp1
emp1.update(emp2)
print("-" * 40)
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("clear".center(40, "-"))
emp1 = {'empid': 1289, 'empname': 'Kevin', 'age': 34, 'dept': 'Finance', 'sal': 85000}
print(f"emp1 :{emp1}")
emp1.clear()
print("-" * 40)
print(f"emp1 :{emp1}")


