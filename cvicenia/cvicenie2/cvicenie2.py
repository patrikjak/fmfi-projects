# 1
n = int(input("Zadaj n: "))
for x in range(n+1):
    print(x * "*")

#################################################

# 2
print("\n")
str = input("Zadaj slovo: ")
x = 0
for znak in str:
    x += 1
    print(znak * x)

#################################################

# 3
print("\n")
slovo = input("Zadaj slovo: ")
x = 0
y = ""
for znak in slovo:
    x += 1
    y += znak
    print(y)

#################################################

# 4
print("\n")
slovicko = input("Zadaj slovo: ")
n = int(input("Zadaj n: "))
z = 0
for x in range(n):
    print("    " * (z % 4) + slovicko)
    z += 1

#################################################

# 5
print("\n")
ciselko = int(input("Zadaj n: "))
medzery = ciselko - 1
for x in range(ciselko):
    for y in range(medzery):
        print(end=" ")
    medzery -= 1
    for z in range(x+1):
        print("*", end=" ")
    print(" ")

#################################################

# 7
print("\n")
cislo = input("Zadaj cislo: ")
cif_sucet = 0
for x in cislo:
    cif_sucet += int(x)
    print("cifra", x)
print("ciferny sucet je: ", cif_sucet)

#################################################

# 8
print("\n")
pocet_hviezd = int(input("Zadaj n: "))
for x in range(pocet_hviezd):
    for j in range(x+1):
        print("*", end="")
    print(end=" ")

#################################################

# 9
print("\n")
od = int(input("Zadaj od: "))
do = int(input("Zadaj do: ")) + 1
for x in range(od, do):
    print(end=f"<{x}>")
    print(end=" ")

#################################################

# 10
print("\n")
cislo_od = int(input("Zadaj od: "))
cislo_do = int(input("Zadaj do: ")) + 1
for i in range(cislo_od, cislo_do):
        print(f'{i:3} {i**2:5} {i**3:7} {i**4:10}')

#################################################

# 11
print("\n")
pocet = int(input("Zadaj pocet: "))
vysledok = 0
znamienko = 1
for i in range(1, pocet + 1):
    vysledok += znamienko/(2*i-1)
    znamienko *= -1
print(vysledok * 4)

#################################################

# 12
print("\n")
samohlasky = input("Zadaj samohlasky: ")
for znak in samohlasky:
    print(f"S{znak}d{znak} m{znak}ch{znak} n{znak} st{znak}n{znak}, s{znak}d{znak} {znak} sp{znak}.")

#################################################

# 14
print("\n")
uhol_od = int(input("Zadaj od: "))
uhol_do = int(input("Zadaj do: "))
uhol_krok = int(input("Zadaj krok: "))
import math
for i in range(uhol_od, uhol_do + uhol_krok, uhol_krok):
    sinus = math.sin(math.radians(i)) ** 2
    cosinus = math.cos(math.radians(i)) ** 2
    sucet = sinus + cosinus
    print(f"{i:6} sin**2={sinus:6.4f} cos**2={cosinus:6.4f} sucet={sucet}")

#################################################

# 15
print("\n")
pocet_vzdial = int(input("Zadaj n: "))
import random
for i in range(pocet_vzdial):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    vzdialenost = a - b
    print("Prvy bod na priamke je", a, "druhy bod je", b, "Ich vzialenost je ", abs(vzdialenost))

#################################################

# 16
print("\n")
stanice = int(input("Zadaj n:"))
vlak = 100
for i in range(stanice):
    nast = random.randint(0, 9)
    vyst = random.randint(0, 9)
    zostatok = vlak + nast - vyst
    print("Vo vlaku bolo", vlak, "ludi,", nast, "nastupilo,", vyst, "vystupilo. Zostalo", zostatok)
    vlak = zostatok

#################################################

# 17
print("\n")
riadky = int(input("Zadaj pocet riadkov: "))
stlpce = int(input("Zadaj pocet stlpce: "))
sprava = ""
mimozemstan = ""
for i in range(1, riadky + 1):
    sprava = ""
    for j in range(stlpce):
        mimozemstan = random.choice("0-")
        sprava += mimozemstan
    print(sprava)

#################################################

# 18
print("\n")
hody = int(input("Zadaj n: "))
for i in range(hody):
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    sucet = kocka1 + kocka2
    print("Na 1. kocke padlo cislo", kocka1)
    print("Na 2. kocke padlo cislo", kocka2)
    print("Ich sucet je", sucet)
    print("================================")

#################################################

# 19
print("\n")
poc_hody = int(input("Zadaj n: "))
poc_kociek = int(input("Zadaj pocet kociek: "))
for i in range(poc_hody):
    sucet_kociek = 0
    for j in range(1, poc_kociek + 1):
        nahodne_cislo = random.randint(1, 6)
        sucet_kociek += nahodne_cislo
        print(f"Na {j}. kocke padla {nahodne_cislo}")
    print("Ich sucet je", sucet_kociek)
    print("========================")

#################################################

# 20
print("\n")
n = int(input('Zadaj n: '))
for i in range(n):
    for k in range(3):
        for j in range(n):
            print(f'{i*n + j + 1:2}', end=' ')
        print(end=" ")
    print("")