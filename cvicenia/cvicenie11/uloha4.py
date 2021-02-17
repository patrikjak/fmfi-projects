import turtle
import random
t = turtle.Turtle()
t.pu()
t.setposition(-200, 0)
t.pd()


def strom(kmen, koruna):
    t.seth(90)
    t.color('brown')
    t.pensize(15)
    t.forward(kmen)
    t.color('green')
    t.pensize(40)
    t.forward(koruna)
    t.pu()
    t.backward(kmen+koruna)
    t.seth(360)


for i in range(8):
    strom(random.randint(30, 60), random.randint(10, 40))
    t.pu()
    t.fd(50)
    t.pd()
turtle.mainloop()
