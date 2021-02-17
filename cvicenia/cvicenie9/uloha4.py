def desiatkova(cislo):
    ciselko = str(cislo)
    zoznam = []
    for i, cifra in enumerate(ciselko):
        zoznam.append(int(cifra))
    return zoznam


print(desiatkova(11213))
