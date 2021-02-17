import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x1, y1, x2, y2 = 100, 50, 200, 100
obdlznik = canvas.create_rectangle(x1, y1, x2, y2, fill="yellow", outline="yellow")
farby = ['blue', 'red', 'green', 'yellow']


def klik(event):
    if (x1 <= event.x <= x2) and (y1 <= event.y <= y2):
        canvas.itemconfig(obdlznik, fill=farby[0], outline=farby[0])
        prva = farby[0]
        farby.pop(0)
        farby.append(prva)
        

canvas.bind('<ButtonPress-1>', klik)

canvas.mainloop()
