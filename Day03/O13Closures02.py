

def addMe(x, y):
    return x + y

res = addMe(10, 20)
print(f"res :{res}")

print("-" * 40)

# closure
def outerFun(info):             # HOF - Higher Order Function
    inf = f"Mr. {info}"

    def innerFun():
        print(inf)

    return innerFun

outerFun("Sachin")
print("-" * 40)

print(outerFun.__name__)
print(outerFun("Sachin").__name__)
print("-" * 40)

outerFun("Sachin")()

print("-" * 40)

inFun = outerFun("Sachin")
print("hello world")
print("before calling the innerFun")

inFun()
