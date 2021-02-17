def pascalov_trojuholnik(n):
    vysledok = []
    for i in range(n):
        vysledok.append([1])
        for j in range(1, i):
            vysledok[i].append(vysledok[i-1][j-1] + vysledok[i-1][j])
        if i != 0:
            vysledok[i].append(1)
    return vysledok


def vypis(tab, sirka=4):
    for riadok in tab:
        for prvok in riadok:
            print(f"{repr(prvok):>{sirka}}", end=' ')
        print()


pt = pascalov_trojuholnik(5)
vypis(pt)
