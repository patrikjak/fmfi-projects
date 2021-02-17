import turtle
t = turtle.Turtle()
t.pu()
t.setposition(-200, 0)
t.pd()
t.rt(90)


def polkruzinca(velkost, smer):
    for i in range(36):
        if i < 18:
            t.fd(velkost)
            if smer:
                t.lt(360/36)
            else:
                t.rt(360/36)


smer = True
opacny = not smer
for i in range(10):
    polkruzinca(3, smer)
    smer, opacny = opacny, smer
turtle.mainloop()
