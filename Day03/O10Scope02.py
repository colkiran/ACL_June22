
# global Scope

glbX = 100

def fun(x):
    global glbX                     # global variable
    glbX = 500
    print(x)
    y = "World"
    print(f"Inside :{glbX}")
    # glbX = 500                     # local variable with same as name as global variable
    z = x + y
    print(z)

print(f"Before :{glbX}")

fun("Hello")

print(f"After :{glbX}")