def stvorec(n, znak):
    print(n * znak)
    for i in range(n - 2):
        print(znak, end="")
        for j in range(n - 2):
            print(end=" ")
        print(znak)
    print(n * znak)


stvorec(5, "O")
