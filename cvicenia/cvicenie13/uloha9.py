def citaj(meno_suboru):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    riadok = subor.readline()
    vysledok = []
    while riadok != "":
        arr = riadok.split()
        vysledok.append(arr)
        riadok = subor.readline()
    return vysledok


print(citaj('subory/text1.txt'))
