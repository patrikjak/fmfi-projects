import tkinter
canvas = tkinter.Canvas(width="350", height="300")
canvas.pack()

medzera = 20
sirka = 135
vyska = 90

canvas.create_rectangle(medzera, medzera, medzera + sirka, medzera + vyska)
canvas.create_rectangle(medzera, medzera, medzera + sirka, medzera + (vyska/3), fill="black")
canvas.create_rectangle(medzera, medzera + (vyska/3), medzera + sirka, medzera + 2*(vyska/3), fill="red", outline="red")
canvas.create_rectangle(medzera, medzera + 2*(vyska/3), medzera + sirka, medzera + 3*(vyska/3), fill="yellow", outline="yellow")

canvas.create_rectangle(2*medzera + sirka, medzera, 2*medzera + 2*sirka, medzera + vyska)
canvas.create_rectangle(2*medzera + sirka, medzera, (2*medzera + ((2*sirka) - 2*(sirka / 3))), medzera + vyska, fill="green", outline="green")
canvas.create_rectangle(2*medzera + sirka + (sirka/3), medzera, (2*medzera + ((2*sirka) - (sirka / 3))), medzera + vyska, fill="white", outline="white")
canvas.create_rectangle(2*medzera + sirka + 2*(sirka/3), medzera, 2*medzera + 2*sirka, medzera + vyska, fill="red", outline="red")

canvas.create_rectangle(medzera, 2*medzera + vyska, medzera + sirka, 2*medzera + 2 * vyska)
canvas.create_rectangle(medzera, 2*medzera + vyska, medzera + sirka - 2*(sirka/3), 2*medzera + 2*vyska, fill="blue", outline="blue")
canvas.create_rectangle(medzera + (sirka/3), 2*medzera + vyska, medzera + sirka - (sirka/3), 2*medzera + 2 * vyska, fill="white", outline="white")
canvas.create_rectangle(medzera + 2*(sirka/3), 2*medzera + vyska, medzera + sirka, 2*medzera + 2 * vyska, fill="red", outline="red")

canvas.create_rectangle(2*medzera + sirka, 2*medzera + vyska, 2*medzera + 2*sirka, 2*medzera + 2*vyska)
canvas.create_rectangle(2*medzera + sirka, 2*medzera + vyska, 2*medzera + 2*sirka, 2*medzera + 2*vyska - 2*(vyska/3), fill="white", outline="white")
canvas.create_rectangle(2*medzera + sirka, 2*medzera + vyska + (vyska/3), 2*medzera + 2*sirka, 2*medzera + 2*vyska - (vyska/3), fill="blue", outline="blue")
canvas.create_rectangle(2*medzera + sirka, 2*medzera + vyska + 2*(vyska/3), 2*medzera + 2*sirka, 2*medzera + 2*vyska, fill="red", outline="red")

canvas.mainloop()