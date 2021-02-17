import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x, y = 50, 50
a1, a2 = 180, 100
canvas.create_rectangle(x, y, x + a1, y + a1, fill="indian red")
canvas.create_text(x - 5, y - 5, text="A")
canvas.create_text(x + a1 + 5, y - 5, text="B")
canvas.create_text(x + a1 + 5, y + a1 + 5, text="C")
canvas.create_text(x - 5, y + a1 + 5, text="D")
canvas.create_text(x + a1 + 10, y + (a1/2), text=a1)
canvas.create_rectangle(x + ((a1 - a2) / 2), y + ((a1 - a2) / 2), x + a2 + ((a1 - a2) / 2), y + a2 + ((a1 - a2) / 2), fill="light blue")
canvas.create_text(x + (a1 / 2), y + ((a1 / 2) + a2 / 2) - 10, text=a2)

canvas.mainloop()