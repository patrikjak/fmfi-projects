def zoznam_suctov(tab):
    vys_zoznam = []
    for i in range(len(tab)):
        suma = ""
        suma_num = 0
        suma_tuple = ()
        if not tab[i]:
            vys_zoznam.append(None)
            continue
        for j in range(len(tab[i])):
            if type(tab[i][j]) == str:
                suma += tab[i][j]
            elif type(tab[i][j]) == int or type(tab[i][j]) == float:
                suma_num += tab[i][j]
            elif type(tab[i][j]) == tuple:
                suma_tuple += tab[i][j]
        if suma != "":
            vys_zoznam.append(suma)
        elif suma_tuple != ():
            vys_zoznam.append(suma_tuple)
        elif type(suma_num) == int or type(suma_num) == float:
            vys_zoznam.append(suma_num)
    return vys_zoznam


print(zoznam_suctov([['1', 'x', '2'], [], [5, 6], [3.1, 4], [(5, 6), (7,)]]))
