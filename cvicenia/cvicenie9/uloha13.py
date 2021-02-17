def zoznam_cisel(retazec):
    zoznam_str = retazec.split()
    novy_zoznam = []
    for i in range(len(zoznam_str)):
        novy_zoznam.append(int(zoznam_str[i]))
    return novy_zoznam


print(zoznam_cisel('12 345 6 -78 9000'))
