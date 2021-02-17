# 5. zadanie: najcastejsie
# autor: Patrik Jakab
# datum: 3.11.2020

tab = []


def citaj(meno_suboru):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    vsetky = []
    cely_subor = subor.read()
    slova = cely_subor.split()
    vsetky_bez = []
    opakovane = []
    bez_duplikat = []
    for i in slova:
        if i not in vsetky_bez:
            vsetky_bez.append(i)
        else:
            opakovane.append(i)
    for i in opakovane:
        if i not in bez_duplikat:
            bez_duplikat.append(i)
    for i in vsetky_bez:
        if i not in bez_duplikat:
            vsetky.append((i, 1))
    for i in vsetky:
        tab.append(i)
    for i in bez_duplikat:
        tab.append((i, slova.count(i)))

    subor.close()

def pocet_vyskytov(slovo):
    ret_val = 0
    for i in tab:
        if i[0] == slovo:
            ret_val = i[1]
    return ret_val


def najcastejsie():
    maxim = 0
    vys_ntica = []
    for i in tab:
        if i[1] >= maxim:
            maxim = i[1]
    for i in tab:
        if i[1] == maxim:
            vys_ntica.append(i[0])
    return tuple(vys_ntica)


def s_poctom(n):
    vys_ntcia = []
    for i in tab:
        if i[1] == n:
            vys_ntcia.append(i[0])
    return tuple(vys_ntcia)


def najdlhsie():
    maxim = 0
    vys_ntica = []
    for i in tab:
        if len(i[0]) > maxim:
            maxim = len(i[0])
    for i in tab:
        if len(i[0]) == maxim:
            vys_ntica.append(i[0])
    return tuple(vys_ntica)


def najkratsie():
    vys_ntica = []
    minim = len(tab[0][0])
    for i in tab:
        if len(i[0]) < minim:
            minim = len(i[0])
    for i in tab:
        if len(i[0]) == minim:
            vys_ntica.append(i[0])
    return tuple(vys_ntica)


def s_dlzkou(n):
    vys_ntcia = []
    for i in tab:
        if len(i[0]) == n:
            vys_ntcia.append(i[0])
    return tuple(vys_ntcia)


# citaj('subory/projekt5/text5.txt')
# print('pocet vyskytov "the":', pocet_vyskytov('the'))
# print('najcastejsie:', najcastejsie())
# print('najdlhsie:', najdlhsie())
# print('najkratsie:', najkratsie())
# print('len s poctom 5:', s_poctom(5))
# print('len s poctom 10:', s_poctom(10))
# print('len s dlzkou 10:', s_dlzkou(10))
# print('pocet roznych slov =', len(tab))
