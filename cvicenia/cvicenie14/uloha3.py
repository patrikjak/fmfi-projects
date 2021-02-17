class Cas:

    def __init__(self, hodiny, minuty):
        self.hodiny = hodiny
        self.minuty = minuty

    def vypis(self):
        print(f"Cas je {self.hodiny:02}:{self.minuty:02}")

    def str(self):
        return f"{str(self.hodiny):>02}:{str(self.minuty):>02}"

    def pridaj(self, hodiny, minuty):
        hod = self.hodiny
        min = self.minuty

        pripocitane_min = min + minuty
        pripocitane_hod = hod + hodiny

        if pripocitane_min > 60:
            pripocitane_hod += 1
            zobrate = 60 - min
            pripocitane_min = abs(zobrate - minuty)
            self.hodiny = pripocitane_hod
            self.minuty = pripocitane_min
        elif pripocitane_min == 60:
            pripocitane_hod += 1
            pripocitane_min = 0
            self.hodiny = pripocitane_hod
            self.minuty = pripocitane_min
        else:
            self.hodiny = pripocitane_hod
            self.minuty = pripocitane_min


c = Cas(17, 40)
print('teraz je', c.str())
c.pridaj(1, 35)
print('neskôr', c.str())
