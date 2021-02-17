import tkinter
canvas = tkinter.Canvas(width="500", height="400")
canvas.pack()

znak = tkinter.PhotoImage(file="sk.png")
x, y = 30, 30
sir, vys = 325, 216
modra, cervena = '#0b4ea2', '#ee1c25'

canvas.create_rectangle(x, y, x + sir, y+vys)
canvas.create_rectangle(x, y, x + sir, y+vys, fill="#ffffff", outline="#ffffff")
canvas.create_rectangle(x, y + (vys/3), x + sir, y+vys, fill=modra, outline=modra)
canvas.create_rectangle(x, y + 2*(vys/3), x + sir, y+vys, fill=cervena, outline=cervena)
canvas.create_image(100 + x, 108 + y, image=znak)

canvas.mainloop()