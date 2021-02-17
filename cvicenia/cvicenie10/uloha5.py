import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

body = []


def klik(event):
    global body
    x, y = event.x, event.y
    farba = f'#{random.randrange(256 ** 3):06x}'
    canvas.create_text(x, y, text="+")
    body.append((x, y))
    if len(body) >= 3:
        if abs(body[0][0] - body[len(body)-1][0]) < 5 or abs(body[0][1] - body[len(body)-1][1]) < 5:
            canvas.create_polygon(body, fill=farba)
            body.clear()


canvas.bind('<ButtonPress-1>', klik)

canvas.mainloop()
