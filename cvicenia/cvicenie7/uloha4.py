meno = input("Zadaj nazov suboru: ")
subor = open(meno, 'r', encoding="utf-8")
print("Riadky s troma slovami:")
riadok = subor.readline()
while riadok != "":
    pocet_medzier = 0
    for i in range(len(riadok)):
        if riadok[i] == " ":
            pocet_medzier += 1
    if pocet_medzier == 2:
        print(end=riadok)
    riadok = subor.readline()
