def cele(hodnota):
    try:
        return int(hodnota)
    except (ValueError, TypeError, NameError, OverflowError):
        return 0


print(cele(12.3))
print(cele('13'))
print(cele([]))
print(cele('12.3'))
