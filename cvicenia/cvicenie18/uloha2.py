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


class MojaTurtle0(MojaTurtle):

    def lt(self, uhol):
        super().lt(uhol+random.randint(-5, 5))

    def rt(self, uhol):
        super().rt(uhol+random.randint(-5, 5))


class MojaTurtle1(MojaTurtle0):
    def fd(self, dlzka):
        while dlzka >= 5:
            self.lt(60)
            super().fd(5)
            self.rt(120)
            super().fd(5)
            self.lt(60)
            dlzka -= 5
        super().fd(dlzka)


class MojaTurtle2(MojaTurtle0):
    def fd(self, dlzka):
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)


turtle.delay(0)
for i in range(20):
    MojaTurtle2().domcek(50)

turtle.mainloop()
