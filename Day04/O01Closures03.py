
def outerFun(greet):

    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")

# simple curry
KanGreet = outerFun("Namaskara")
SpanGreet = outerFun("Hola")

KanGreet("Rahul Dravid")
KanGreet("Anil Kumble")
KanGreet("KL Rahul")
SpanGreet("Messi")

