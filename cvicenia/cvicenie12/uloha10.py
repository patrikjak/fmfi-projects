import turtle
t = turtle.Turtle()
t.pu()
t.bk(50)
t.pd()


def vypisane4(n, a):
    if n == 0:
        return
    else:
        for i in range(4):
            t.fd(a)
            t.lt(90)
        t.fd(a/2)
        t.lt(45)
        d = (a/2)**2 + (a/2)**2
        vypisane4(n-1, d**(1/2))


vypisane4(4, 200)
turtle.mainloop()
