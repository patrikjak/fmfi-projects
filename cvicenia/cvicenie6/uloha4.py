def postupnost(start, koniec, krok=1):
    print("\"", end="")
    for i in range(start, koniec, krok):
        if i == koniec - krok:
            print(str(i), end="")
        else:
            print(str(i), end=" ")
    print("\"", end="")


postupnost(13, 5, -2)
