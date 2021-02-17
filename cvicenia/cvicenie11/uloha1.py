import turtle
import random

turtle.delay(0)
t = turtle.Turtle()


def bodka(velkost, farba):
    # for i in range(100):
    #     x = random.randint(-300, 300)
    #     y = random.randint(-300, 300)
    #     t.penup()
    #     t.setposition(x, y)
    #     t.pendown()
    #     pomer = random.randrange(3)
    #     if pomer == 0:
    #         t.color('#ff0000')
    #         t.pensize(50)
    #     else:
    #         t.color('#0000ff')
    #         t.pensize(30)
    #     t.forward(0)

    t.penup()
    t.setposition(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    t.pensize(velkost)
    t.color(farba)
    t.forward(0)


bodka(50, '#ff0000')
t.dot(50, '#0000ff')
turtle.mainloop()
