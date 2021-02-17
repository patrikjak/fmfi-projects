import turtle
import random
t = turtle.Turtle()
t.pu()
t.setposition(-200, 0)
t.pd()


def kocka(d):
    for i in range(3):
        farba = f"#{random.randrange(256 ** 2):06x}"
        if i == 0:
            t.fillcolor(farba)
            t.begin_fill()
            for j in range(4):
                t.fd(d)
                t.rt(-90)
            t.end_fill()
        elif i == 1:
            t.fd(d)
            t.fillcolor(farba)
            t.begin_fill()
            for j in range(4):
                t.rt(-45)
                if j == 1:
                    t.fd(d)
                    t.rt(-90)
                elif j == 3:
                    t.fd(d)
                else:
                    t.fd(d/2)
            t.end_fill()
        elif i == 2:
            t.rt(180)
            t.fillcolor(farba)
            t.begin_fill()
            t.backward(-d)
            t.rt(45)
            t.fd(d / 2)
            t.rt(-135)
            t.fd(d)
            t.rt(-45)
            t.fd(d/2)
            t.rt(-135)
            t.fd(d)
            t.end_fill()
    t.rt(90)
    t.fd(d)
    t.rt(-90)


for i in range(4):
    kocka(50)
    t.pu()
    t.fd(75)
    t.pd()
turtle.mainloop()
