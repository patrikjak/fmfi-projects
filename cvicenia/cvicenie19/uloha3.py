skladatel = {}
with open('subory/skladatelia.txt') as file:
    riadok = file.readline()
    while riadok != "":
        riadok_list = riadok.split()
        skladatel[riadok_list[0]] = riadok_list[1]
        riadok = file.readline()
min = int(list(skladatel.values())[0])
max = 0
meno_max, meno_min = "", ""
for kluc, hodnota in skladatel.items():
    if int(hodnota) > max:
        max = int(hodnota)
        meno_max = kluc
    if int(hodnota) < min:
        min = int(hodnota)
        meno_min = kluc


def medzi(rok1, rok2):
    zoz = []
    for kluc, hodnota in skladatel.items():
        if rok1 < int(hodnota) < rok2:
            zoz.append(kluc)
    return zoz


print("najstarsi je:", meno_max, max)
print("najmladsi je:", meno_min, min)
print(medzi(1720, 1730))
print(medzi(1820, 1830))
