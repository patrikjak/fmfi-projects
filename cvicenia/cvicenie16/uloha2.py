class Zviera:

    def __init__(self, meno):
        self._meno = meno.capitalize()

    def __str__(self):
        return f"Zviera {self._typ} ma meno {self._meno} a robi {self._zvuk}"
    
    @property
    def meno(self):
        return self._meno

    @meno.setter
    def meno(self, meno):
        self._meno = meno.capitalize()

    @property
    def zvuk(self):
        return self._zvuk

    @zvuk.setter
    def zvuk(self, zvuk):
        if "-" in zvuk:
            self._zvuk = zvuk
        else:
            self._zvuk = f"{zvuk}-{zvuk}"

    @property
    def typ(self):
        return self._typ


class Pes(Zviera):
    _typ = "pes"
    _zvuk = "haf-haf"


class Macka(Zviera):
    _typ = "macka"
    _zvuk = "mnau-mnau"


class Kacka(Zviera):
    _typ = "kacka"
    _zvuk = "ga-ga"


z1 = Pes('dunčo')
z2 = Macka('mica')
z3 = Pes('bono')
z4 = Kacka('gréta')
z3.zvuk = 'vrr'
z4.meno = 'grETA'
# z2.typ = 'cat'
print(z3)
print(z4)
print(z2)
