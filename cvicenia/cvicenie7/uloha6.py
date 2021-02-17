def priemer(meno_suboru):
    subor = open(meno_suboru, 'r')
    riadok = subor.readline()
    sucet, pocet = 0, 0
    while riadok != "":
        pocet += 1
        sucet += int(riadok)
        riadok = subor.readline()
    subor.close()
    priemerik = sucet / pocet
    return priemerik


print("Priemer:", priemer("subory/cisla.txt"))