def sucet(priklad):
    if priklad.find('+'):
        sek = 0
        spolu = 0
        for i, znak in enumerate(priklad):
            if znak == "+":
                spolu += int(priklad[sek:i])
                sek = i + 1
        posledne_cislo = int(priklad[sek:])
        spolu += posledne_cislo
        print(spolu)
    else:
        print(int(priklad))


sucet("1+2+3+4+5")
