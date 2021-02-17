# 7. zadanie: zoznamy
# autor: Patrik Jakab
# datum: 20.11.2020

vysledky = [0, [], [], [], []]


def pocet_zoznamov(param, vymaz=True):
    for i in range(len(param)):
        if type(param[i]) == list:
            vysledky[0] += 1
            pocet_zoznamov(param[i], False)
    vys = vysledky[0] + 1
    if vymaz:
        vysledky[0] = 0
    return vys


def zoznam_prvkov(zoznam, vymaz=True):
    for i in range(len(zoznam)):
        if type(zoznam[i]) != list:
            vysledky[1].append(zoznam[i])
        else:
            zoznam_prvkov(zoznam[i], False)
    vys = vysledky[1]
    if vymaz:
        vysledky[1] = []
    return vys


def splosti(zoznam, vymaz=True):
    for i in range(len(zoznam)):
        if type(zoznam[i]) != list:
            vysledky[2].append(zoznam[i])
        else:
            splosti(zoznam[i], False)
    zoznam.clear()
    for i in range(len(vysledky[2])):
        zoznam.append(vysledky[2][i])
    if vymaz:
        vysledky[2].clear()


# zoznam by nemal by modified
def nahradeny_zoznam(zoznam, hodnota1, hodnota2, vymaz=True):
    for i in range(len(zoznam)):
        if type(zoznam[i]) == list:
            nahradeny_zoznam(zoznam[i], hodnota1, hodnota2, False)
        if zoznam[i] == hodnota1:
            zoznam[i] = hodnota2
        if vymaz:
            vysledky[3].append(zoznam[i])
    vys = vysledky[3].copy()
    if vymaz:
        vysledky[3].clear()
    return vys


def nahrad(zoznam, hodnota1, hodnota2, vymaz=True):
    for i in range(len(zoznam)):
        if type(zoznam[i]) == list:
            nahradeny_zoznam(zoznam[i], hodnota1, hodnota2, False)
        if zoznam[i] == hodnota1:
            zoznam[i] = hodnota2
        if vymaz:
            vysledky[4].append(zoznam[i])
    zoznam.clear()
    for i in range(len(vysledky[4])):
        zoznam.append(vysledky[4][i])
    if vymaz:
        vysledky[4] = []


zoz = [[[7]], 8]
print(nahradeny_zoznam(zoz, 7, 'a'))
print(nahradeny_zoznam([1, 2, 3, [1, 2], 3, [[[1]]], [], 2], 1, 'x'))
print(nahradeny_zoznam([3, [33, [333, [13], 13]], 36], 3, 'q'))
print(nahradeny_zoznam([3, [33, [333, [13], 13]], 36], [13], 'm'))
