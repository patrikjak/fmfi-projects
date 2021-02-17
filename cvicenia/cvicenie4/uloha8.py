import tkinter

canvas = tkinter.Canvas()
canvas.pack()

n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 12
        if (i == j) or (j == 12-i):  # if i == 6 or j == 6
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)

canvas.mainloop()