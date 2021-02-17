cislo = int(input("Zadaj cislo: "))
print(cislo, '=', end=" ")
for delitel in range(2, cislo + 1):
    while cislo % delitel == 0:
        print(delitel, end="")
        cislo = cislo/delitel
        if cislo != 1:
            print(end=" * ")