import tkinter
canvas = tkinter.Canvas()
canvas.pack()


def kresli(event):
    dlzka = 100/2
    canvas.create_line(event.x - dlzka, event.y, event.x + dlzka, event.y)


def zmaz(event):
    canvas.delete('all')


canvas.bind('<B1-Motion>', kresli)
canvas.bind('<ButtonPress-3>', zmaz)

canvas.mainloop()
