meno = input("Zadaj meno suboru: ")
subor = open(meno, 'r', encoding="utf-8")
for i in range(2):
    riadok = subor.readline()
    if i == 1:
        print("Druhý riadok súboru je:", repr(riadok.rstrip()))

subor.close()