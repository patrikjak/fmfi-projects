a = [2, 3, '5', 7, 11]


def posun(zoznam):
    prvy = zoznam[0]
    zoznam.remove(prvy)
    zoznam.append(prvy)


posun(a)
print(a)
zoz = 'kto druhemu jamu kope'.split()
print()
for i in range(5):
    print(zoz)
    posun(zoz)
