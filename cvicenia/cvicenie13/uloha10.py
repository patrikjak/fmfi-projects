def zapis(tab, meno_suboru):
    subor = open(meno_suboru, 'w', encoding="utf-8")
    for i in range(len(tab)):
        riadok = ""
        for j in range(len(tab[i])):
            if j != len(tab[i]) - 1:
                riadok += str(tab[i][j]) + " "
            else:
                riadok += str(tab[i][j])
        if i != len(tab) - 1:
            subor.write(riadok+"\n")
        else:
            subor.write(riadok)


x = [['Anička', 'dušička'], ['kde', 'si', 'bola'], ['keď', 'si', 'si', 'čižmičky'], ['zarosila']]
zapis(x, 'subory/text2.txt')
zapis([[1, 11, 21], [345], [-5, 10]], 'subory/cisla.txt')
