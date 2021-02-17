def riadok(n, text=""):
    if text != "":
        dlzka = len(text)
        dlzka += 2
        pocet_hviedz = n - dlzka
        print("*" * int((pocet_hviedz / 2)), end=" ")
        print(text, end=" ")
        if dlzka % 2 == 0:
            print("*" * int((pocet_hviedz / 2)), end="")
        else:
            print("*" * int((pocet_hviedz / 2)), end="*")
        print()
    else:
        print("*" * n)

riadok(50)
riadok(50, "Ján Botto")
riadok(50, "Žltá ľalija")
riadok(50, "-")
riadok(50, "Stojí stojí mohyla")
riadok(50, "Na mohyle zlá chvíľa")
riadok(50, "na mohyle tŕnie chrastie")
riadok(50, "a v tom tŕní chrastí rastie")
riadok(50)