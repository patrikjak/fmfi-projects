def z_dvojkovej(cislo):
    binarne = ""
    for i in range(len(cislo)):
        binarne += str(cislo[i])
    return int(binarne, 2)


print(z_dvojkovej([1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1]))
