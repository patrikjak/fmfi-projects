def vypis(tab, sirka=4):
    for riadok in tab:
        for prvok in riadok:
            print(f"{repr(prvok):>{sirka}}", end=' ')
        print()


vypis([[1, 6, 3.14], [0.5, 1.5, 2.5]], 7)
print()
vypis([[1, 2, 3], [None, None], ['4', '5', '6'], ['Python', 3.9]])
