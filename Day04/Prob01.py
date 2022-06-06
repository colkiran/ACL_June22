
from datetime import datetime

def decorator_timer(some_function):
    def wrapper(x):
        t1 = datetime.now()
        some_function(x)
        t2 = datetime.now()
        result = t2 - t1
        print(f"Total time taken is {result}")
    return wrapper


@decorator_timer
def add(a):
    l = []
    for i in range(a):
        for j in range(1, i + 1):
            l.append(j ** 2)

add(7000)