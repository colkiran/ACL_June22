
def outerFun(greet):

    def innerFun(seprt):

        def innerMostFun(gname):
            import emojis
            emojized = emojis.encode(greet + " :" + seprt + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun


engGrt = outerFun("Welcome")
tigerImg = engGrt("tiger")
tigerImg("Prabhakar")
tigerImg("Sheroff")

elphImg = engGrt("elephant")
elphImg("Micheal")

"""
outerFun("Welcome") ("----->")("Sachin")

EngGrt = outerFun("Welcome")
dblArrowE = EngGrt("=====>>")

TmlGrt = outerFun("Vanankam")
starArrowTm = TmlGrt("*******>>")

dblArrowE("Rahul Dravid")
starArrowTm("Ravichandran Ashwin")
"""