import turtle
t = turtle.Turtle()


def domcek(d):
    prepona = ((d/2) ** 2 + (d/2) ** 2) ** (1/2)
    t.rt(-90)
    t.fd(d)
    t.rt(90)
    t.fd(d)
    t.rt(-135)
    t.fd(prepona)
    t.rt(-90)
    t.fd(prepona)
    t.rt(-90)
    t.fd(prepona*2)
    t.rt(-135)
    t.fd(d)
    t.rt(-135)
    t.fd(prepona * 2)
    t.rt(-135)
    t.fd(d)


t.rt(5)
domcek(100)
domcek(50)
domcek(80)
turtle.mainloop()
