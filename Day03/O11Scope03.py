
# nested functions
"""
outerFun is called the parent of innerFun
innerFun is within the scope of outerFun
only a local variable can be converted into a non-local variable
"""

x = 100                         # global variable

def outerFun(gname):            # local variable
    print(f"Before :{gname}")

    def innerFun():
        nonlocal gname          # nonlocal variable
        print("Hello World....")
        gname += " Dravid"
        print(f"Welcome {gname}")

    innerFun()
    print(f"After :{gname}")

outerFun("Rahul")