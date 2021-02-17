def citaj_cisla(meno_suboru):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    riadok = subor.readline()
    vysledok = []
    while riadok != "":
        arr = riadok.split()
        vysledok.append(arr)
        riadok = subor.readline()
    for i in range(len(vysledok)):
        for j in range(len(vysledok[i])):
            vysledok[i][j] = int(vysledok[i][j])
    return vysledok


print(citaj_cisla('subory/cisla.txt'))
