def male(retazec, i):
    uprava_male = ""
    for j, znak in enumerate(retazec):
        if j == i:
            uprava_male += retazec[i].lower()
        else:
            uprava_male += znak
    print(uprava_male)


def velke(retazec, i):
    uprava_velke = ""
    for j, znak in enumerate(retazec):
        if j == i:
            uprava_velke += retazec[i].upper()
        else:
            uprava_velke += znak
    print(uprava_velke)


male("Python", 0)
velke("Python", 5)