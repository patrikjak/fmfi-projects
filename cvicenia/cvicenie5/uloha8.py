import random

def hadanie(od, do):
    print("Myslim si cislo, uhadni ho...")
    cislo = random.randint(od, do)
    pokus_cislo = 0
    while pokus_cislo < 10:
        pokus = int(input("Tvoj tip: "))
        pokus_cislo += 1
        if pokus > cislo:
            print("*** uber")
        elif pokus < cislo:
            print("*** pridaj")
        elif pokus == cislo:
            print(f"Uhadol si na {pokus_cislo}. pokus. Gratulujem")
            break
    else:
        print("Neuhadol si ani na 10. pokus")
        print("Myslel som si cislo", cislo)


hadanie(0, 500)