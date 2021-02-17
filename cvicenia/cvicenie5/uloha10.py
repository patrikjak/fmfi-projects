import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()


def kruhy(x,y):
    for i in reversed(range(0, 10)):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        farba = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_oval(x-(i*5), y-(i*5), x+(i*5), y+(i*5), fill=farba)


for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))

canvas.mainloop()