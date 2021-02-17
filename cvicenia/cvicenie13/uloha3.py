def zoznam_suctov(tab):
    vys_zoznam = []
    for i in range(len(tab)):
        vys_zoznam.append(sum(tab[i]))
    return vys_zoznam


print(zoznam_suctov([[1, 2, 3], [4], [], [5, 6]]))
