import tkinter
canvas = tkinter.Canvas()
canvas.pack()

zoznam = [200, 100, "Python"]


def kresli_text(zoznam):
    x = zoznam[0]
    y = zoznam[1]
    text = zoznam[2]
    if len(zoznam) > 3:
        canvas.create_text(x, y, text=text, font=zoznam[3])
    else:
        canvas.create_text(x, y, text=text, font="arial 20")


kresli_text(zoznam)
kresli_text([200, 150, 'programovanie', 'consolas 35'])
kresli_text([200, 60, 'najlepšie je', 'tahoma 15'])

canvas.mainloop()
