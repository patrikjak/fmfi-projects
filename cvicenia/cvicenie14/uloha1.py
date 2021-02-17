class Cas:

    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        print(f"Cas je {self.hodiny:02}:{self.minuty:02}")


c = Cas(9, 17)
c.vypis()
d = Cas(10, 5)
d.vypis()
