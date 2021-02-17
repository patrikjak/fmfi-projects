import turtle
import random
t = turtle.Turtle()
t.pu()
t.setposition(-200, 0)
t.pd()


def stvorec(velkost):
    t.fillcolor(f"#{random.randrange(256 ** 3):06x}")
    t.begin_fill()
    for j in range(4):
        t.forward(velkost)
        t.rt(-90)
    t.forward(velkost)
    t.end_fill()


for i in range(10):
    stvorec(random.randint(20, 50))
turtle.mainloop()
