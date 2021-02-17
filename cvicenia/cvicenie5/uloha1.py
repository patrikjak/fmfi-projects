def obdlznik(sirka, znak="*"):
    for i in range(sirka):
        print(znak, end="")
    print()
    print(znak, end="")
    for i in range(1, sirka - 1):
        print(end=" ")
    print(znak)
    for i in range(sirka):
        print(znak, end="")

obdlznik(10, "#")