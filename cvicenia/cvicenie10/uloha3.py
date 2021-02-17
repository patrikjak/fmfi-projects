import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

xx = yy = None


def klik(event):
    global xx, yy
    x, y = event.x, event.y
    if xx is not None and yy is not None:
        farba = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(xx, yy, x, y, fill=farba, outline=farba)
        xx = yy = None
    else:
        xx, yy = x, y


canvas.bind('<ButtonPress-1>', klik)

canvas.mainloop()
