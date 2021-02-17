def max2(tab):
    maxi = max(tab[0])
    for i in range(len(tab)):
        if max(tab[i]) > maxi:
            maxi = max(tab[i])
    print(maxi)


def min2(tab):
    mini = min(tab[0])
    for i in range(len(tab)):
        if min(tab[i]) < mini:
            mini = min(tab[i])
    print(mini)


def sum2(tab):
    suma = 0
    for i in range(len(tab)):
        suma += sum(tab[i])
    print(suma)


p = [[1, 6, 3.14], [0.5, 1.5, 2.5]]
r = [[-1, -2], [-3, -4]]
max2(p)
min2(p)
sum2(p)
max2(r)
min2(r)
sum2(r)
