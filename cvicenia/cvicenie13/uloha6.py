def preklop(tab):
    vys_tab = []
    for i in range(len(tab[0])):
        novy_riadok = []
        for j in range(len(tab)):
            novy_riadok.append(tab[j][i])
        vys_tab.append(novy_riadok)
    return vys_tab


def vypis(tab, sirka=4):
    for riadok in tab:
        for prvok in riadok:
            print(f"{repr(prvok):>{sirka}}", end=' ')
        print()


p = [[1, 2, 4], [5, 6, 7], [3, 4, 1], [8, 9, 4]]
vypis(preklop(p), 2)
