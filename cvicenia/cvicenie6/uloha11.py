def riadky(retazec):
    riadok = 0
    rez = 0
    for i in range(len(retazec)):
        if retazec[i] == "\n":
            riadok += 1
            print(f"{riadok}. ", retazec[rez:i])
            rez = i
    print(f"{riadok+1}. {retazec[rez+1:]}")


riadky("toto je prvy riadok\n\na toto je treti riadok\na toto zasa stvrty")