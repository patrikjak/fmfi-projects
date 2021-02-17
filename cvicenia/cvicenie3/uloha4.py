import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

x, y = 250, 250
farba, farba2, farba3 = "red", "blue", "yellow"
for i in reversed(range(10, 200, 10)):
    farba, farba2 = farba2, farba
    canvas.create_rectangle(x-i, y-i, x+i, y+i, fill=farba)
    farba2, farba3 = farba3, farba2

canvas.mainloop()