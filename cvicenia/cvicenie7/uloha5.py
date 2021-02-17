meno = input("Zadaj nazov suboru: ")
subor = open(meno, 'r', encoding="utf-8")
riadok = subor.readline()
print("Druhé slová:")
while riadok != "":
    pocet_medzier = 0
    cut = 0
    for i in range(len(riadok)):
        if riadok[i] == " ":
            pocet_medzier += 1
            if pocet_medzier == 2:
                print(riadok[cut + 1:i])
                break
            cut = i

    riadok = subor.readline()

subor.close()