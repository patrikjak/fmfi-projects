import random


def dve_kocky(pocet):
    zoznam = [0] * 13
    for i in range(pocet):
        hod_1 = random.randint(1, 6)
        hod_2 = random.randint(1, 6)
        sucet = hod_1 + hod_2
        zoznam[sucet] += 1
    return zoznam


print(dve_kocky(1000))
