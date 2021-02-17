# 4. zadanie: zarovnaj
# autor: Patrik Jakab
# datum: 30.10.2020

def spracovanie(meno_suboru, sirka, hladane_slovo="", sirka_plus=0):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    odsekovy_subor, upraveny_subor = "", ""
    cely_subor = subor.read()
    for i, znak in enumerate(cely_subor):
        if i < len(cely_subor) - 1:
            if cely_subor[i] == "\n" and cely_subor[i + 1] == "\n" and cely_subor[i - 1] == "\n":
                pass
            elif cely_subor[i] == " " and cely_subor[i - 1] == " ":
                pass
            elif cely_subor[i] == " " and cely_subor[i - 1] == "\n":
                pass
            else:
                upraveny_subor += znak

    for i, znak in enumerate(upraveny_subor):
        if i < len(upraveny_subor) - 1:
            if upraveny_subor[i] == "\n" and upraveny_subor[i + 1] != "\n" and upraveny_subor[i - 1] != "\n":
                odsekovy_subor += " "
            elif upraveny_subor[i] == "\n" and upraveny_subor[i + 1] == "\n":
                odsekovy_subor += "\n"
            else:
                odsekovy_subor += znak

    start_cut, end_cut = 0, 0
    odseky = []
    for i, znak in enumerate(odsekovy_subor):
        if odsekovy_subor[i] == "\n":
            end_cut = i + 1
            odsek = odsekovy_subor[start_cut:end_cut]
            odseky.append(odsek)
            start_cut = i + 1
    odseky.append(odsekovy_subor[start_cut:])

    slovicka = []
    slovo = ""
    cut = 0

    for i in range(len(odseky)):
        slovicka.append([])
        for j in range(len(odseky[i])):
            if odseky[i][j] == " ":
                slovicka[i].append(slovo)
                slovo = ""
                cut = j + 1
            elif odseky[i][j] == "\n":
                slovo += "\n"
                slovicka[i].append(slovo)
                slovo = ""
            else:
                slovo += odseky[i][j]
    slovicka[len(slovicka) - 1].append(odseky[len(odseky) - 1][cut:])

    vymazat = []
    realne_slovicka = []
    if hladane_slovo != "":
        for i in range(len(slovicka)):
            zapisat = False
            for j in range(len(slovicka[i])):
                if slovicka[i][j].find(hladane_slovo) > -1:
                    zapisat = True
            if zapisat:
                vymazat.append(i)
        for i in range(len(vymazat)):
            index = vymazat[i]
            realne_slovicka.append(slovicka[index])
            if i != len(vymazat) -1:
                realne_slovicka.append(["\n"])
        slovicka = realne_slovicka

    riadok_arr = []

    for i in range(len(slovicka)):
        pocet = 0
        riadok = ""
        riadok_upraveny = []
        for j in range(len(slovicka[i])):
            if len(slovicka[i]) - 1 == j:
                pocet += len(slovicka[i][j])
                if len(slovicka[i]) != 1 and i != len(slovicka) - 1:
                    pocet -= 1
            else:
                pocet += len(slovicka[i][j]) + 1
            if pocet <= sirka + sirka_plus:
                riadok += slovicka[i][j]
                if len(slovicka[i]) - 1 != j:
                    riadok += " "
                if j <= len(slovicka[i]) - 2:
                    if len(slovicka[i]) - 2 != j:
                        dlzka_riadka_nasl = len(riadok) + len(slovicka[i][j + 1]) + 1
                    else:
                        dlzka_riadka_nasl = len(riadok) + len(slovicka[i][j + 1]) - 1
                    if dlzka_riadka_nasl > sirka + sirka_plus:
                        if riadok[-1] == " ":
                            riadok = riadok[:-1]
                        riadok += "\n"
                        riadok_upraveny.append(riadok)
                        pocet = 0
                        riadok = ""
        if riadok[-1] == " ":
            riadok = riadok[:-1]
        riadok_upraveny.append(riadok)
        riadok_arr.append(riadok_upraveny)

    return riadok_arr


def vypis(meno_suboru, sirka, zarovnat=True, slovo=''):
    if zarovnat:
        spracovany_arr = spracovanie(meno_suboru, sirka, slovo)
        komplet_subor = ""
        for i in range(len(spracovany_arr)):
            for j in range(len(spracovany_arr[i])):
                if len(spracovany_arr[i]) - 1 != j:
                    pocet_medzier = sirka - (len(spracovany_arr[i][j]) - 1)
                    medzery = []
                    zostatok_medzier = pocet_medzier
                    for k in range(len(spracovany_arr[i][j])):
                        if spracovany_arr[i][j][k] == " ":
                            medzery.append(k + 1)
                    for k in range(len(spracovany_arr[i][j])):
                        if len(spracovany_arr[i][j]) - 1 < sirka:
                            komplet_subor += spracovany_arr[i][j][k]
                            if spracovany_arr[i][j][k] == " ":
                                if pocet_medzier == 1:
                                    if k + 1 == medzery[0]:
                                        komplet_subor += " "
                                else:
                                    komplet_subor += " " * (pocet_medzier // len(medzery))
                                    zostatok_medzier -= (pocet_medzier // len(medzery))
                                    if zostatok_medzier == 1:
                                        komplet_subor += " "
                        else:
                            komplet_subor += spracovany_arr[i][j][k]
                else:
                    for k in range(len(spracovany_arr[i][j])):
                        komplet_subor += spracovany_arr[i][j][k]

        print(komplet_subor)

    else:
        spracovany_arr = spracovanie(meno_suboru, sirka, slovo, 1)
        for i in range(len(spracovany_arr)):
            for j in range(len(spracovany_arr[i])):
                print(end=spracovany_arr[i][j])


vypis("subory/projekt4/subor1.txt", 20, True, "")
