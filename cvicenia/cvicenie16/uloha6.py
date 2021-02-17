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


class MojaTurtle1(MojaTurtle):

    def fd(self, dlzka):
        while dlzka >= 5:
            self.lt(60)
            super().fd(5)
            self.rt(120)
            super().fd(5)
            self.lt(60)
            dlzka -= 5
        super().fd(dlzka)


class MojaTurtle2(MojaTurtle):

    def fd(self, dlzka):
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)


start = -300
for i in range(10):
    nahoda = random.randrange(3)
    if nahoda == 0:
        MojaTurtle(start + (i * 50), 100).domcek(random.randrange(30, 50))
    elif nahoda == 1:
        MojaTurtle1(start + (i * 50), 100).domcek(random.randrange(30, 50))
    else:
        MojaTurtle2(start + (i * 50), 100).domcek(random.randrange(30, 50))
