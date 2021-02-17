def posun_znak(znak, posun):
    cislo_znaku = ord(znak)
    cislo_znaku += posun
    vysledny_znak = chr(cislo_znaku)
    print(vysledny_znak)


posun_znak("c", 4)
