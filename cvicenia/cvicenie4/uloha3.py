poradie = 0
sucet = 0
while 1:
    poradie += 1
    ciselko = float(input(f"Zadaj {poradie}. cislo: "))
    sucet += ciselko
    if ciselko == 0:
        break
print("súčet všetkých prečítaných čísel je", sucet)
