def palindrom(retazec):
    string = retazec.replace(" ", "")
    string = string.lower()
    if len(string) == 1:
        return True
    if string[0] == string[-1]:
        return palindrom(string[1:-1])
    else:
        return False


print(palindrom("Jelenovi pivo nelej"))
