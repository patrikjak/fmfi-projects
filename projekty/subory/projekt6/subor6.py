import turtle
t = turtle.Turtle()
t.pensize(3)
for _ in range(360):
    t.fd(2)
    t.lt(1)
t.pensize(1)
t.fd(300)
turtle.mainloop()