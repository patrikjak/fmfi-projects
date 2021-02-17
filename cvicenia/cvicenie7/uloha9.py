def ity(meno_suboru, index):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    riadok = subor.readline()
    riadok_cislo = -1
    while riadok != "":
        riadok_cislo += 1
        if riadok_cislo == index:
            return repr(riadok.lstrip())
        riadok = subor.readline()

    subor.close()


print(ity("subory/text1.txt", 2))
