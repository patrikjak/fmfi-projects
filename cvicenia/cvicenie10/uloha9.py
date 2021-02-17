import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()


def klik(event):
    farba = f'#{random.randrange(256 ** 3):06x}'
    x_stvorcek = event.x // 50
    y_stvorcek = event.y // 50
    canvas.create_rectangle(50 * x_stvorcek, 50 * y_stvorcek, (50 * x_stvorcek) + 50, (50 * y_stvorcek) + 50, fill=farba, outline=farba)


canvas.bind('<ButtonPress-1>', klik)

canvas.mainloop()
