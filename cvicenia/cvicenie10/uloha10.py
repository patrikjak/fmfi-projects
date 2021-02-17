import tkinter
canvas = tkinter.Canvas()
canvas.pack()

r, x0, y0 = 120, 150, 130
kruh = canvas.create_oval(x0 + r, y0 + r, x0 - r, y0 - r, fill="#ffffff")


def farbicka(event):
    vzd_x = abs(x0 - event.x) ** 2
    vzd_y = abs(y0 - event.y) ** 2
    vzd = (vzd_x + vzd_y) ** (1/2)
    if vzd <= r:
        f = int(255 * vzd / r)
        canvas.itemconfig(kruh, fill=f"#{f:02x}{f:02x}{f:02x}")


canvas.bind('<Motion>', farbicka)

canvas.mainloop()
