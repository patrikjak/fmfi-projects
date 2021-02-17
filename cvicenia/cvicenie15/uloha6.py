import tkinter


class Klikanie:

    kliky = []

    def __init__(self):
        self.canvas = tkinter.Canvas()
        self.canvas.pack()
        self.canvas.bind('<ButtonPress>', self.klik)

    def klik(self, event):
        self.canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5)
        self.kliky.append((event.x, event.y))
        if len(self.kliky) % 3 == 0:
            self.vypis()

    def vypis(self):
        for i in range(len(self.kliky)):
            print(self.kliky[i])


k = Klikanie()
tkinter.mainloop()
