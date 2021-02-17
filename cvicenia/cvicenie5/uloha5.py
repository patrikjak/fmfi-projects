def fib_medzi(od, do):
    a, b = 0, 1
    while do:
        a, b = b, a + b
        if od < b < do:
            print(b, end=" ")
        do -= 1


fib_medzi(10, 100)