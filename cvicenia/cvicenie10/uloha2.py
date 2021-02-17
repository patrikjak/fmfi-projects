import tkinter
canvas = tkinter.Canvas()
canvas.pack()

polomer = 0


def kresli(event):
    global polomer
    polomer += 1
    if polomer != None:
        canvas.create_oval(event.x + polomer, event.y + polomer, event.x - polomer, event.y - polomer, fill="yellow")


def zmaz(event):
    canvas.delete('all')
    global polomer
    if polomer != None:
        polomer = 1


canvas.bind('<B1-Motion>', kresli)
canvas.bind('<ButtonPress-3>', zmaz)

canvas.mainloop()
