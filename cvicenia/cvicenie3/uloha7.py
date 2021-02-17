import tkinter
canvas = tkinter.Canvas(width="400", height="300")
canvas.pack()

x1, y1 = 10, 100
x2, y2 = 30, 120
d = 20

for i in range(16):
    canvas.create_line(x1, y1, x1 + d, y1 + d, fill="blue", width=5)
    canvas.create_line(x2, y2, x2 + d, y2 - d, fill="blue", width=5)
    x1 += d
    y1 *= -1
    x2 += d
    y2 *= -1

canvas.mainloop()