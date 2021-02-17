def mocnina(n, k):
    if k == 0:
        return 1
    elif k < 0:
        return
    else:
        return mocnina(n, k - 1) * n


print(mocnina(2, 900))
print(2**900)
