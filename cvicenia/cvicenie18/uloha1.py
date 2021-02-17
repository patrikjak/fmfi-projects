import turtle
import random


class MojaTurtle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        super().speed(0)
        super().pu()
        super().setposition(random.randrange(-250, 250), random.randrange(-250, 250))
        super().pd()

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


turtle.delay(0)
for i in range(30):
    MojaTurtle1().domcek(30)
