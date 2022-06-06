
def funLogger(fnc):

    def helper():
        print("My Info logged into a service......")
        fnc()
        print("My Info logged out of the service.....")

    return helper

def normalFun():
    print("I should be called as normal....")

funLogger(normalFun)            # no Output
print("-" * 40)
funLogger(normalFun)()

print("-" * 40)
res_fun = funLogger(normalFun)
res_fun()

print("-" * 40)
normalFun = funLogger(normalFun)
normalFun()


print("-" * 40)
@funLogger              # Decorator
def basicFun():
    print("I should be called basic.....")

basicFun()
# basicFun = funLogger(basicFun)
# basicFun()
