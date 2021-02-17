cislo = int(input("Zadaj cislo: "))
cs = 0
while cislo:
    cs += cislo % 10
    print(cislo % 10)
    cislo //= 10
print("ciferny sucet =", cs)