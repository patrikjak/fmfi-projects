import turtle
t = turtle.Turtle()
for _ in range(8):
    for _ in range(2):
        for _ in range(9):
            t.fd(9)
            t.lt(10)
        t.lt(90)
    t.rt(45)
turtle.mainloop()