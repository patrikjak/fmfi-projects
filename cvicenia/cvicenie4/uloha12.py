import tkinter
import random

canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()

for i in range(10000):
    x = random.randint(1, 300)
    y = random.randint(1, 300)
    if (x > 75 and x < 225) and (y > 75 and y < 225):
        farba = 'red'
    else:
        farba = 'blue'
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=farba, width=0)

canvas.mainloop()