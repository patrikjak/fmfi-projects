import tkinter
canvas = tkinter.Canvas()
canvas.pack()

pole = []


def klik(event):
    if len(pole) == 0:
        pole.append(1)
        canvas.create_text(event.x, event.y, text=pole[len(pole) - 1])
    else:
        pole.append(len(pole) + 1)
        canvas.create_text(event.x, event.y, text=pole[len(pole) - 1])


canvas.bind('<ButtonPress-1>', klik)

canvas.mainloop()
