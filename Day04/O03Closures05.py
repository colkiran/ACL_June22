
def fun1(*args):
    print(args, "\n", *args)
    print("-" * 40)

fun1(1, 2, 3, 4, 5)
fun1(1)
fun1()
print("-" * 40)

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def prod(x, y):
    return x * y

def log_details(fnc):               # HOF
    logInfo = "Logging into the sevice....."

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 40)

    return innerFun

sum_logger = log_details(sum)
diff_logger = log_details(diff)
prod_logger = log_details(prod)

sum_logger(10, 20)         # calls the innerFun with args
diff_logger(40, 15)
prod_logger(30, 20)
