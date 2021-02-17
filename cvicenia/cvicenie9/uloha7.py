import random


def nahodne_body(pocet):
    zoznam = []
    for i in range(pocet):
        x, y = random.randint(0, 380), random.randint(0, 260)
        suradnice = ()
        suradnice += (x, y)
        zoznam.append(suradnice)
    return zoznam


print(nahodne_body(5))
