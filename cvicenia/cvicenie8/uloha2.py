domy = [4, 2, 0, 5, 0, 1, 5, 4]
max_obyv = 0
max_dom = 0
obyvatelia = 0
neobyvane = 0
for i in range(len(domy)):
    max_obyv = max(domy)
    max_dom = domy.count(max_obyv)
    obyvatelia += domy[i]
    neobyvane = domy.count(0)
print("pocet obyvatelov je:", obyvatelia)
print("neobyvanych domov je:", neobyvane)
print("maximalny pocet obyvatelov v dome je:", max_obyv)
print("pocet maximalnych domov je:", max_dom)