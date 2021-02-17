import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()


def stv(riadok, stlpec, farba="white"):
    canvas.create_rectangle(5+(30*stlpec), 5+(30*riadok), 35+(30*stlpec), 35+(30*riadok), fill=farba, outline=farba)


def nahodna_farba():
    for i in range(256):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        nah_farba = f"#{r:02x}{g:02x}{b:02x}"
    return nah_farba


def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


for i in range(8):
    for j in range(12):
        if i == j:
            stv(i, j, rgb(255, 20 * j, 0))
        else:
            stv(i, j, rgb(255, 20 * j, 0))


canvas.mainloop()