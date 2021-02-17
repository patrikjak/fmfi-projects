class Ucet:

    def __init__(self, meno, suma=0):
        self._meno = meno
        self._suma = suma

    def __str__(self):
        return f"Ucet {self._meno} -> {self._suma}"

    def stav(self):
        return self._suma

    def vklad(self, suma):
        self._suma += suma

    def vyber(self, suma):
        if suma > 0:
            if suma <= self._suma:
                self._suma -= suma
                return suma
            else:
                vyber = self._suma
                self._suma = 0
                return vyber
        else:
            pass


mbank = Ucet('mbank')
csob = Ucet('csob', 100)
tatra = Ucet('tatra', 17)
sporo = Ucet('sporo', 50)
mbank.vklad(sporo.vyber(30) + tatra.vyber(30))
csob.vyber(-5)
spolu = 0
for ucet in mbank, csob, tatra, sporo:
    print(ucet)
    spolu += ucet.stav()
print('spolu = ', spolu)
