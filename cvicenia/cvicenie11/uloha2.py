import turtle
t = turtle.Turtle()


def slnko(pocet, velkost):
    t.dot(velkost, 'gold')
    t.color('gold')
    t.pensize(10)
    uhol = 360 / pocet
    for i in range(1, pocet + 1):
        t.seth(uhol * i)
        t.forward(velkost)
        t.back(velkost)


slnko(10, 150)
turtle.mainloop()
