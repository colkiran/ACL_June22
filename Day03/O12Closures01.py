
# closures
def outerFun(gname):
    info = f"Mr. {gname}"

    def innerFun():

        print("Hello World.....")
        print(f"Greetings {gname}")
        print(f"Greetings {info}")

    innerFun()

outerFun("Sachin")
