import tkinter
import random
canvas = tkinter.Canvas(width="500", height="400")
canvas.pack()

sucet = 0
y = 20

for i in range(10):
    hodnota = random.choice((1, 2, 5, 10, 20, 50))
    sucet += hodnota
    canvas.create_rectangle(20, y, 70, y + 20, fill="white")
    canvas.create_text(45, y + 10, text=f"{hodnota} €", fill="black", font=("Arial", 15))
    y += 25

canvas.create_text(300, 50, text=f"spolu = {sucet} €", font=("Arial", 25))

canvas.mainloop()