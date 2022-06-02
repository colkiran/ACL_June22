
from collections import namedtuple

nmdTpl = namedtuple("Employee", "empid empname gender dept sal")
emp = nmdTpl(empid= 243, empname="Richard", gender="M", dept="HR", sal=95000)

print(emp)
print("-" * 40)

print(f"Empid   :{emp.empid}")
print(f"Empname :{emp.empname}")
print(f"Gender  :{emp.gender}")
print(f"Department :{emp.dept}")
print(f"Salary  :{emp.sal}")


