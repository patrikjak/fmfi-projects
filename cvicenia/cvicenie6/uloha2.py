def sucet(prikladik):
    prve_cislo = prikladik[:prikladik.find('+')]
    druhe_cislo = prikladik[len(prve_cislo)+1:]
    prve_cislo = int(prve_cislo)
    druhe_cislo = int(druhe_cislo)
    spolu = prve_cislo + druhe_cislo
    print(spolu)


sucet("25+15")
