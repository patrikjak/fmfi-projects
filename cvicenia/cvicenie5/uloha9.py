import tkinter


def koleso(x, y, priemer=15, farba="blue"):
    canvas.create_oval(x - priemer, y - priemer, x + priemer, y + priemer, fill=farba)


def doska(x, y, dlzka=100, vyska=25, farba="red"):
    canvas.create_rectangle(x - (dlzka/2), y, x + (dlzka/2), y - vyska, fill=farba)


def vozik(x, y):
    doska(x, y)
    koleso(x-30, y)
    koleso(x+30, y)


def velky_vozik(x, y):
    doska(x, y, 150, 40, 'green')
    koleso(x-35, y, 25, 'orange')
    koleso(x+35, y, 25, 'orange')


canvas = tkinter.Canvas()
canvas.pack()

vozik(200, 100)
velky_vozik(150, 200)
vozik(300, 210)

canvas.mainloop()