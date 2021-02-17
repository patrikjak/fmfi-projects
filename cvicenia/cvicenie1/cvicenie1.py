a1 = 3**(1/2)
a2 = 5**((1/3)/1/3)
a3 = (1024**(1/5))**5
a4 = (2**20)**(1/10)

print("a1 = ", a1)
print("a2 = ", a2)
print("a3 = ", a3)
print("a4 = ", a4)
print("\n")

##############################################

pi = 3.141592653589793

print("Pi = ", pi)
print("\n")
print(223/71)  # najmensi rozdiel
print((22/17)+(37/47)+(88/83))
print((99**2)/(2206*(2**(1/2))))
print((((5 ** (1 / 2)) + 6) ** (1 / 2) + 7) ** (1 / 2))
print(((10**100)/11222.11122)**(1/192))

##############################################

print("\n")
name = input("zadaj meno: ")
age = int(input("zadaj vek: "))
print(name, "má ", age, "rokov")
print(name, "bude mať o rok", age + 1, "rokov")
print(name, "bude mať o 10 rokov", age + 10, "rokov")

##############################################

print("\n")
r = float(input("Zadaj polomer kruhu: "))
print("Obvod kruhu je: ", 2*pi*r)
print("Obsah kruhu je: ", pi*(r**2))

##############################################

print("\n")
dlzka = float(input("Zadaj dlzku strany kocky: "))
sten = round((dlzka ** 2 + dlzka ** 2) ** (1/2), 2)
tele = round((sten ** 2 + dlzka ** 2) ** (1/2), 2)
print("Stenova uhlopriecka kocky je:", sten)
print("Telesova uhlopriecka kocky je:", tele)

##############################################

print("\n")
ciselko = int(input("Zadaj ciselko: "))
print(ciselko // 10, ciselko % 10)
print(ciselko // 100, ciselko % 100)
print(ciselko // 1000, ciselko % 1000)
print(ciselko // 10000, ciselko % 10000)

##############################################

print("\n")
prve_slovo = input("Zadaj prve slovo: ")
druhe_slovo = input("Zadaj druhe slovo: ")
tretie_slovo = input("Zadaj tretie slovo: ")
print(prve_slovo, druhe_slovo, tretie_slovo)
print(prve_slovo, tretie_slovo, druhe_slovo)
print(druhe_slovo, prve_slovo, tretie_slovo)
print(druhe_slovo, tretie_slovo, prve_slovo)
print(tretie_slovo, prve_slovo, druhe_slovo)
print(tretie_slovo, druhe_slovo, prve_slovo)

##############################################

print("\n")
txt = input("Zadaj nejaky text: ")
print((txt + "\n") * 10)

##############################################

print("\n")
dni = (11 * 365) + (8 * 30) + 21
hodiny = dni * 24
sekundy = hodiny * 60 * 60
print("Pocet dni je: ", dni)
print("Pocet hodin je: ", hodiny)
print("Pocet sekund je: ", sekundy)

##############################################

print("\n")
bajty = int(input("Zadaj pocet bajtov: "))
print((256 ** bajty) - 1)

##############################################

print("\n")
n = int(input("Zadaj n: "))
print("Na ", n, ". policku bude ", (n-1) * (n-1), "zrniek ryze")

##############################################

print("\n")
prve = input("Zadaj prve cislo: ")
druhe = input("Zadaj druhe cislo: ")
prve_cislo = int(prve)
druhe_cislo = int(druhe)
vysledok_cislo = prve_cislo + druhe_cislo
vysledok = str(vysledok_cislo)
print(prve + "+" + druhe + "=" + vysledok)
