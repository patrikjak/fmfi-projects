meno = input("Zadaj meno suboru: ")
subor = open(meno, 'r', encoding="utf-8")
riadok = subor.readline()
print(end="Kazdy druhy znak: '")
for i in range(len(riadok)):
    if i % 2 != 0:
        print(end=riadok[i])

print("'")
subor.close()