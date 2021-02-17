class Cas:

    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        print(f"Cas je {self.hodiny:02}:{self.minuty:02}")

    def str(self):
        return f"{str(self.hodiny):>02}:{str(self.minuty):>02}"


c = Cas(9, 1)
print("Teraz je", c.str())
