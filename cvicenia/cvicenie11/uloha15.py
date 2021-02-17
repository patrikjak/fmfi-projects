import turtle
import random
import math
t = turtle.Turtle()


def stvorec(velkost, preklopit):
    farba = f"#{random.randrange(256 ** 3):06x}"
    t.fillcolor(farba)
    t.begin_fill()
    for j in range(4):
        t.forward(velkost)
        if preklopit:
            t.rt(-270)
        else:
            t.rt(-90)
    t.end_fill()


def pytagoras(prepona, uhol):
    odvesna1 = prepona * math.sin(math.radians(uhol))
    odvesna2 = prepona * math.cos(math.radians(uhol))
    print("Stvorec nad preponou:", prepona*prepona)
    print("Stvorec nad prvou odvesnou:", odvesna1*odvesna1)
    print("Stvorec nad druhou odvesnou:", odvesna2*odvesna2)
    print("Sucet:", odvesna1*odvesna1 + odvesna2*odvesna2)
    t.rt(-uhol)
    stvorec(prepona, False)
    t.rt(uhol)
    stvorec(odvesna2, True)
    t.rt(odvesna2)
    t.seth(0)
    t.fd(odvesna2)
    stvorec(odvesna1, False)


pytagoras(150, 15)
turtle.mainloop()
