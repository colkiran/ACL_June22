
def greet():
    print("Greetings Mr. Sachin Welcome to the Event.....")

def greetGst(gname):
    print(f"Greetings Mr. {gname}, Welcome to the Event.......")

# city is a default argument and gname is a non default argument
# non default argument cannot follow a default argument

def greetGstCity(gname, city="Mumbai"):
    print(f"Greetings Mr. {gname} from {city}, Welcome to the Event.......")

greet()
greetGst("Rahul")
greetGstCity("Sachin")
greetGstCity("Rohit")
greetGstCity("Kholi", "Delhi")

print("-" * 40)
def admission(fname, lname, dob, conno, city, idprof):
    print(f'Name :{fname} {lname}')
    print(f"Date of Birth :{dob}")
    print(f"Contact no :{conno}")
    print(f"City :{city}")
    print(f"ID Proof :{idprof}")

admission(city = "Mumbai", fname= 'Sachin', lname="Temdulkar", idprof="PAN Card", conno='998898998', dob="06/9/1988")

# return values
# ---------------

print("-" * 40)
def Multply_ME(x, y):
    return x * y

a = 10
b = 20
print(f"the product {a} and {b} is {Multply_ME(a, b)}")

print("-" * 40)

def arithmetic_Calc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmetic_Calc(10, 5)
print(f"res :{res}")

# Variable length arguments

print("-" * 40)
def productAll(*numbers):
    print(numbers)
    print(*numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = productAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)
def extract_details(**detail):
    print(detail)
    for i in detail:
        print(i, "=>", detail[i])

extract_details(name="sachin", runs=145, oppn='sri lanka', venue="galle")

print("-" * 40)

def enroll(cname, *tech, **marks):
    print(f"Name :{cname}")
    print("Technologies :", tech)
    print("Marks :", marks)


enroll("Mike", 'Java', 'j2ee', 'spring', 'hibernate', 'angularJS', 'reactJS',
       xth='79%', xiith='83%', degree='75%', pg='85%')

print("-" * 40)
# Document String
def fun():
    "This is a document String"
    # This is a comment
    print("Hello World")

fun()
print(fun.__doc__)          # doc string

print("#" * 40)

def fun1(a, b):
    """
    Function Name - fun1
    fun1 takes two arguments 'a' and 'b' which is of type integers
    fun1 returns the sum of these two numbers as results

    example:
    30 = fun1(10, 20)

    """
    return a + b

print(fun1(10, 20))

print("#" * 40)

help(fun1)