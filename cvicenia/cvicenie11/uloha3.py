import turtle
t = turtle.Turtle()


def terc(pocet):
    farba1 = '#0000ff'
    farba2 = 'yellow'
    velkost = 15 * pocet
    for i in range(pocet):
        t.dot(velkost, farba1)
        velkost -= 15
        farba1, farba2 = farba2, farba1


terc(40)
turtle.mainloop()
