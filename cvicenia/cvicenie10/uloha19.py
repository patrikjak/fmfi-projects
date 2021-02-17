import tkinter
import time
canvas = tkinter.Canvas(width="500", height="300")
canvas.pack()

h, m, s = time.localtime()[3:6]
d = 0
cas = canvas.create_text(250, 150, text=f"{h}:{m}:{s}.{d}", font=("arial", 50))


def update():
    global h, m, s, d
    d += 1
    if d == 9:
        d = 0
    h, m, s = time.localtime()[3:6]
    canvas.itemconfig(cas, text=f"{h}:{m}:{s}.{d}")
    canvas.after(1, update)


update()

canvas.mainloop()
