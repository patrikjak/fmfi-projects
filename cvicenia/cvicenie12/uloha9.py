import turtle
t = turtle.Turtle()
t.pu()
t.bk(150)
t.pd()


def vpisane3(n, a):
    if n == 0:
        return
    else:
        for i in range(3):
            t.fd(a)
            t.lt(120)
        t.fd(a/2)
        t.lt(60)
        vpisane3(n-1, a/2)


vpisane3(4, 300)
turtle.mainloop()
