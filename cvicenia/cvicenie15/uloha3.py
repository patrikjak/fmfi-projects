import tkinter
import random


class Stv:
    canvas = None

    def __init__(self, x, y, a=20, farba=""):
        self.x = x
        self.y = y
        self.a = a
        if farba == "":
            self.farba = f"#{random.randrange(256 ** 3):06x}"
        else:
            self.farba = farba

        self.id = self.canvas.create_rectangle(self.x - (self.a / 2), self.y - (self.a / 2),
                                               self.x + (self.a / 2), self.y + (self.a / 2), fill=self.farba,
                                               outline=self.farba)

    def __str__(self):
        return f"Stv{self.x, self.y, self.a, self.farba}"

    def posun(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

    def zmen_farbu(self, farba):
        self.farba = farba
        self.canvas.itemconfig(self.id, fill=farba, outline=farba)


Stv.canvas = tkinter.Canvas()
Stv.canvas.pack()
for i in range(30):
    x_rand = random.randint(50, 300)
    y_rand = random.randint(50, 200)
    stvorec = Stv(x_rand, y_rand)
    # print(stvorec)
    # stvorec.posun(10, 0)
    # stvorec.zmen_farbu("yellow")
    # print(stvorec)
tkinter.mainloop()
