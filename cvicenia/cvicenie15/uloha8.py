import tkinter


class Tahanie:

    body = []

    def __init__(self):
        self.canvas = tkinter.Canvas()
        self.canvas.pack()
        self.canvas.bind('<B1-Motion>', self.tahanie)
        self.canvas.bind('<ButtonPress>', self.klik)

    def klik(self, event):
        self.canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5)

    def tahanie(self, event):
        self.body.append((event.x, event.y))
        print(self.body)
        if len(self.body) > 0:
            self.canvas.create_line(self.body[len(self.body) - 2], event.x, event.y)


k = Tahanie()
tkinter.mainloop()
