import tkinter
canvas = tkinter.Canvas(width="500", height="400")
canvas.pack()

x, y = 70, 100
r = 50
dx, dy = 120, 60

canvas.create_oval(x, y, x + r*2, y + r*2, outline="blue", width=15)
canvas.create_oval(x + dx/2, y + dy, x + dx/2 + r*2, y + dy + r*2, outline="yellow", width=15)
canvas.create_oval(x + dx, y, x + dx + r*2, y + r*2, outline="black", width=15)
canvas.create_oval(x + dx/2 + dx, y + dy, x + dx/2 + dx + r*2, y + dy + r*2, outline="green", width=15)
canvas.create_oval(x + 2*dx, y, x + r*2 + 2*dx, y + r*2, outline="red", width=15)

canvas.mainloop()