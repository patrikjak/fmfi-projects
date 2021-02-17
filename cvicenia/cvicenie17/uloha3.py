def desatinne(hodnota):
    try:
        a = float(hodnota)
        return isinstance(a, float)
    except (ValueError, TypeError, NameError, OverflowError):
        return False


print(desatinne('123'))
print(desatinne('  22.7 '))
print(desatinne('22/7'))
