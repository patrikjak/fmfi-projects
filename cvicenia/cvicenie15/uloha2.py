class TelefonnyZoznam:

    zoznam = []

    def __init__(self, meno_suboru):
        self.meno_suboru = meno_suboru

    def pridaj(self, meno, tel):
        zapis = True
        for i in range(len(self.zoznam)):
            if self.zoznam[i][0] == meno:
                self.zoznam[i][1] = tel
                zapis = False
        if zapis:
            self.zoznam.append([meno, tel])

    def change_to_tuple(self):
        for i in range(len(self.zoznam)):
            self.zoznam[i] = tuple(self.zoznam[i])

    def vypis(self):
        for i in range(len(self.zoznam)):
            self.change_to_tuple()
            print(self.zoznam[i][0], self.zoznam[i][1])

    def zapis(self):
        subor = open(self.meno_suboru, 'w', encoding='utf-8')
        for i in range(len(self.zoznam)):
            if i == len(self.zoznam) - 1:
                subor.write(f"{self.zoznam[i][0]};{self.zoznam[i][1]}")
            else:
                subor.write(f"{self.zoznam[i][0]};{self.zoznam[i][1]}\n")
        subor.close()

    def citaj(self):
        subor = open(self.meno_suboru, 'r', encoding="utf-8")
        self.zoznam.clear()
        riadok = subor.readline()
        while riadok != "":
            riadok_arr = riadok.replace("\n", "").split(";")
            self.zoznam.append(tuple(riadok_arr))
            riadok = subor.readline()


tz = TelefonnyZoznam('tel_cisla.txt')
tz.pridaj('Jana', '0901020304')
tz.pridaj('Juro', '0911111111')
tz.pridaj('Jozo', '0212345678')
tz.pridaj('Jana', '0999020304')
tz.zapis()

t2 = TelefonnyZoznam('tel_cisla.txt')
t2.citaj()
t2.vypis()
