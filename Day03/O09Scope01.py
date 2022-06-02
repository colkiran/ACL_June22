
# local

def fun(x):         # x is a local variable
    print(x)
    y = "world"     # y is a local variable
    print(x + y)

fun("Hello ")
# print(x)         # not accessible out of the function


