import turtle
t = turtle.Turtle()
turtle.delay(0)


def nova(position, heading):
    t = turtle.Turtle()
    t.pu()
    t.setpos(position)
    t.seth(heading)
    t.pd()
    return t


def strom(d):
    t.fd(d)
    if d > 20:
        t.lt(40)
        strom(d*.7)
        t.rt(90)
        strom(d*.6)
        t.lt(50)
    else:
        zoznam.append(nova(t.pos(), t.heading()))
    t.fd(-d)


t.lt(90)
t.pu()
t.setpos(0, -200)
t.pd()
zoznam = []
strom(150)
for p in zoznam:
    p.color('green')
    p.shape('turtle')
while True:
    for p in zoznam:
        p.lt(15)
