def pridaj_sucty(tab):
    for i in range(len(tab)):
        suma = ""
        suma_num = 0
        suma_tuple = ()
        if not tab[i]:
            tab[i].append(None)
            continue
        for j in range(len(tab[i])):
            if type(tab[i][j]) == str:
                suma += tab[i][j]
            elif type(tab[i][j]) == int or type(tab[i][j]) == float:
                suma_num += tab[i][j]
            elif type(tab[i][j]) == tuple:
                suma_tuple += tab[i][j]
        if suma != "":
            tab[i].append(suma)
        elif suma_tuple != ():
            tab[i].append(suma_tuple)
        elif type(suma_num) == int or type(suma_num) == float:
            tab[i].append(suma_num)


def vypis(tab, sirka=4):
    for riadok in tab:
        for prvok in riadok:
            print(f"{repr(prvok):>{sirka}}", end=' ')
        print()


t = [['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]
a = [[1, 2, 3], [4], [5, 6]]
pridaj_sucty(a)
vypis(a)
