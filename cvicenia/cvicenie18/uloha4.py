class Cas:

    def __init__(self, hodiny=0, minuty=0, sekundy=0):
        self.sek = abs(3600*hodiny + 60*minuty + sekundy)

    def __str__(self):
        return f'{self.sek // 3600}:{self.sek // 60 % 60:02}:{self.sek % 60:02}'

    def __add__(self, iny):
        if isinstance(iny, int):
            return Cas(sekundy=self.sek+iny)
        elif isinstance(iny, tuple):
            if len(iny) == 1:
                return Cas(sekundy=self.sek + (iny[0] * 3600))
            elif len(iny) == 2:
                return Cas(sekundy=self.sek + (iny[0] * 3600) + (iny[1] * 60))
            elif len(iny) == 3:
                return Cas(sekundy=self.sek+(iny[0] * 3600) + (iny[1] * 60) + iny[2])

    __radd__ = __add__

    def __sub__(self, iny):
        if isinstance(iny, int):
            return Cas(sekundy=self.sek-iny)
        elif isinstance(iny, tuple):
            if len(iny) == 1:
                return Cas(sekundy=self.sek + (iny[0] * 3600))
            elif len(iny) == 2:
                return Cas(sekundy=self.sek + (iny[0] * 3600) + (iny[1] * 60))
            elif len(iny) == 3:
                return Cas(sekundy=self.sek + (iny[0] * 3600) + (iny[1] * 60) + iny[2])

    __rsub__ = __sub__

    def __gt__(self, iny):
        return self.sek > iny.sek

    def __eq__(self, iny):
        return self.sek == iny.sek


c = Cas(8, 10, 34)
print(c)
print(c + 640)
print((1, 55) + c)
print(c - 100)
