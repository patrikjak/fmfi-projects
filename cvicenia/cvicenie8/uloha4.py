zoz = list(range(1, 19))


def vypis(zoznam, pocet):
    k = 0
    poradie = 0
    for i in range(int(len(zoznam) / pocet)):
        for j in range(pocet):
            poradie = k+j
            print(zoznam[poradie], end=" ")
        print()
        k += pocet
    if poradie < len(zoznam):
        for i in range(poradie + 1, len(zoznam)):
            print(zoznam[i], end=" ")


vypis(list("Python"), 2)