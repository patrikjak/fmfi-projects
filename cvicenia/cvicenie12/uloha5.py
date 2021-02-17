def sucet(zoznam):
    if len(zoznam) == 0:
        return 0
    elif len(zoznam) == 1:
        return zoznam[0]
    else:
        stred = len(zoznam) // 2
        pp = sucet(zoznam[:stred])
        dp = sucet(zoznam[stred:])
        return pp + dp


print(sucet([2, 4, 6, 8]))
print(sucet([]))
print(sucet(list(range(500))))
print(sucet(list(range(2000))))
