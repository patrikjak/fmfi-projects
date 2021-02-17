import tkinter
canvas = tkinter.Canvas(width=600)
canvas.pack()

x = 550
y = 50
a = 50

cislo = int(input("Zadaj cislo: "))
while cislo:
    canvas.create_rectangle(x, y, x + a, y + a, fill="#bada55")
    canvas.create_text(x + (a/2), y + (a/2), text=cislo % 10)
    cislo //= 10
    x -= a + 10

canvas.mainloop()