def dvojkova(cislo):
    ciselko = str(cislo)
    ciselko = f"{int(ciselko):b}"
    zoznam = []
    for i, cifra in enumerate(ciselko):
        zoznam.append(int(cifra))
    return zoznam


print(dvojkova(11213))
