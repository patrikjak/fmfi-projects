class Obdlznik:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Obdlznik({self.a},{self.b})"

    def obsah(self):
        return self.a * self.b

    def obvod(self):
        return 2*(self.a + self.b)

    def zmen_velkost(self, pomer):
        self.a *= pomer
        self.b *= pomer

    def kopia(self):
        return Obdlznik(self.a, self.b)


obd1 = Obdlznik(20, 7)
print('obvod =', obd1.obvod())
print(obd1)
obd2 = obd1.kopia()
obd2.zmen_velkost(2)
print(obd2)
