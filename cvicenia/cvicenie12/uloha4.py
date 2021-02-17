def nsd(a, b):
    if b == 0:
        return a
    if a == b:
        return a
    elif a > b:
        return nsd(b, a % b)
    else:
        return nsd(a, b - a)


print(nsd(40, 24))
