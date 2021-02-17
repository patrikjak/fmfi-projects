import tkinter


class Klikanie:

    def __init__(self):
        self.canvas = tkinter.Canvas()
        self.canvas.pack()
        self.canvas.bind('<ButtonPress>', self.klik)

    def klik(self, event):
        self.canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5)


k = Klikanie()
tkinter.mainloop()
