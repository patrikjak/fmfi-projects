import random


def dve_kocky(n):
    vys = {}
    for i in range(n):
        sucet = random.randint(1, 6) + random.randint(1, 6)
        if sucet not in vys:
            vys[sucet] = 1
        else:
            vys[sucet] += 1
    return vys


print(dve_kocky(10))
print(dve_kocky(100))
