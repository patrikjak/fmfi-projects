def posledny_riadok(meno_suboru):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    cut = 0
    cely_subor = subor.read()
    for i, znak in enumerate(cely_subor):
        if znak == "\n":
            cut = i
    if cut < len(cely_subor):
        riadok = cely_subor[cut+1:]
        print(repr(riadok.strip()))
    subor.close()


posledny_riadok("subory/text3.txt")

def predposledny_riadok(meno_suboru):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    start_cut = 0
    end_cut = 0
    cely_subor = subor.read()
    for i, znak in enumerate(cely_subor):
        if znak == "\n" and end_cut > start_cut:
            start_cut = i
        elif znak == "\n":
            end_cut = i

    print(repr(cely_subor[end_cut:start_cut].strip()))
    subor.close()


predposledny_riadok("subory/text3.txt")


def najdlhsi_riadok(meno_suboru):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    riadok = subor.readline()
    max_pismen = 0
    poradie_riadku = 0
    vysledny_riadok = 0
    while riadok != "":
        poradie_riadku += 1
        if len(riadok) > max_pismen:
            max_pismen = len(riadok)
            vysledny_riadok = poradie_riadku
        riadok = subor.readline()
    subor.close()
    subor = open(meno_suboru, 'r', encoding="utf-8")
    for i in range(vysledny_riadok - 1):
        subor.readline()
    naj_riadok = subor.readline()
    print(repr(naj_riadok.strip()))


najdlhsi_riadok("subory/text3.txt")
