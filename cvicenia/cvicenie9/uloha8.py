import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()


def nahodne_body(pocet):
    zoznam = []
    for i in range(pocet):
        x, y = random.randint(0, 380), random.randint(0, 260)
        suradnice = ()
        suradnice += (x, y)
        zoznam.append(suradnice)

    return zoznam


def kreslenie(pocet):
    zoradene = sorted(nahodne_body(pocet))
    for i in range(pocet):
        if i + 1 == pocet:
            canvas.create_line(zoradene[i], zoradene[i])
        else:
            canvas.create_line(zoradene[i], zoradene[i+1])


kreslenie(100)
canvas.mainloop()
