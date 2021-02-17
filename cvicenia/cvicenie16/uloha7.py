import turtle


class Turtle1(turtle.Turtle):

    def trojuholnik(self, strana):
        for i in range(3):
            super().fd(strana)
            super().lt(120)


t = Turtle1()
for i in range(5):
    t.trojuholnik(150)
    t.lt(72)
