import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()


def karticka(x, y, text="python"):
    canvas.create_rectangle(x, y, x+100 , y+40, fill="#cccccc")
    canvas.create_text(x+50, y+20, text=text, font=('arial', 14))

for i in range(10):
    karticka(random.randint(50, 300), random.randint(50, 200), 'Python')

canvas.mainloop()