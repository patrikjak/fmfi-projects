import turtle
import random


class MojaTurtle(turtle.Turtle):

    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()

    def domcek(self, dlzka):
        for uhol in 90, 90, 90, 30, 120, -60:
            self.fd(dlzka)
            self.rt(uhol)


start = -300
for i in range(10):
    MojaTurtle(start + (i * 50), 100).domcek(random.randrange(30, 50))
