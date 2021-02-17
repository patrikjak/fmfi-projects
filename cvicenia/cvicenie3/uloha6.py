import tkinter
canvas = tkinter.Canvas(width="400", height="300")
canvas.pack()

a = 200
b = 50
x = 50
y = 250

hex1 = 0
hex3 = 0

for farba in range(4):
    hex1 += 20
    hex3 += 20
    fill = f"#{hex1}ff{hex3}"
    canvas.create_rectangle(x, y, x + a, y + b, fill=fill)
    y -= b
    x += 25
    a -= b

canvas.mainloop()