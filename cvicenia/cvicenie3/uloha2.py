import tkinter
import random
canvas = tkinter.Canvas(bg="navy", width="400", height="400")
canvas.pack()

for i in range(200):
    velkost = random.randint(10, 20)
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_text(x, y, text="*", fill="yellow", font=("Arial", velkost))

tkinter.mainloop()