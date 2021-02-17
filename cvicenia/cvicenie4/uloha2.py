cislo = int(input("Zadaj cislo: "))

if cislo == 1:
    print(cislo)
else:
    print(cislo, end=", ")
    while cislo != 1:
        if cislo % 2 == 0:
            cislo = cislo / 2
        else:
            cislo = cislo * 3 + 1
        print(int(cislo), end=", ")