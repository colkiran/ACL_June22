
def funLogger(fnc):

    def helper(x, y):

        print("My info logged in a service....")
        res = fnc(x, y)             # callback
        print("My info logged out of the serivce.......")
        return res
    return helper

@funLogger
def add(x, y):
    return x + y

@funLogger
def diff(x, y):
    return x - y

@funLogger
def mul(x, y):
    return x * y


res = add(10, 20)
print(f"res :{res}")

res = diff(30, 16)
print(f"res :{res}")

res = mul(4, 5)
print(f"res :{res}")



print("#" * 40)



def login(fnc):

    def helper(arg):
        print("logged into the system....")
        fnc(arg)
        print("logged out of ths system....")
        print("-" * 40)

    return helper

@login
def deposit(amt):
    print(f"{amt} credited into the account......")

deposit(10000)


