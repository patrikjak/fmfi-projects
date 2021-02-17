import turtle
t = turtle.Turtle()


def kosostvorec(velkost, farba):
    t.fillcolor(farba)
    t.begin_fill()
    for i in range(4):
        t.fd(velkost/2)
        if i == 1:
            t.rt(135)
        else:
            t.rt(45)
    t.end_fill()


farba1 = 'tan'
farba2 = 'tomato'
pocet = 8
for i in range(1, pocet+1):
    kosostvorec(300, farba1)
    t.seth((360/pocet)*i)
    farba1, farba2 = farba2, farba1
turtle.mainloop()
