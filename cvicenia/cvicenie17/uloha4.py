def zoznam(retazec):
    zoz = retazec[1:len(retazec)-1].split(', ')
    vys_zoz = []
    for i in range(len(zoz)):
        try:
            if '.' in zoz[i]:
                vys_zoz.append(float(zoz[i]))
            else:
                vys_zoz.append(int(zoz[i]))
        except ValueError:
            pass

    return vys_zoz


z = zoznam('[0, 1., 2, 3.14]')
print(z)
print(zoznam('[0, -.1, None, +2, [7], a5, -3.14, "8"]'))
