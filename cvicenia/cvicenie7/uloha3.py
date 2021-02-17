meno = input("Zadaj meno suboru: ")
subor = open(meno, 'r', encoding="utf-8")
pocet_riadkov = 0
max_pismenka = 0
riadok = subor.readline()
while riadok != '':
    pocet_riadkov += 1
    if len(riadok) > max_pismenka:
        max_pismenka = len(riadok)
    riadok = subor.readline()

print("Pocet riadkov suboru:", pocet_riadkov)
print("Najdlhsi riadok v subore ma", max_pismenka, "znakov")

subor.close()
print()

subor = open(meno, 'r', encoding="utf-8")
pocet_riadkov = 0
max_pismenka = 0
for riadok in subor:
    pocet_riadkov += 1
    if len(riadok) > max_pismenka:
        max_pismenka = len(riadok)

print("Pocet riadkov suboru:", pocet_riadkov)
print("Najdlhsi riadok v subore ma", max_pismenka, "znakov")

subor.close()
print()

subor = open(meno, 'r', encoding="utf-8")
pocet_riadkov = 0
max_pismenka = 0
cut = 0
cely_subor = subor.read()
for i, znak in enumerate(cely_subor):
    if znak == "\n":
        pocet_riadkov += 1
        riadok = cely_subor[cut:i]
        if len(riadok) > max_pismenka:
            max_pismenka = len(riadok)
        cut = i
if cut < len(cely_subor):
    riadok = cely_subor[cut + 1:]
    if len(riadok) > max_pismenka:
        max_pismenka = len(riadok)

subor.close()

pocet_riadkov += 1

print("Pocet riadkov suboru:", pocet_riadkov)
print("Najdlhsi riadok v subore ma", max_pismenka, "znakov")