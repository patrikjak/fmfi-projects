zoo = {
    "lev": 190,
    "tiger": 300,
    "hyena": 50,
    "gorila": 160,
    "zirafa": 800,
    "simpanz": 50,
    "hroch": 1500,
    "medved": 300,
    "buvol": 590,
    "antilopa": 200,
    "pyton": 90,
    "slon": 5000,
    "gibon": 10,
    "jaguar": 120,
    "jelen": 280,
    "kengura": 80
}


def tazsie_ako(zviera):
    for kluc, hodnota in sorted(zoo.items()):
        if zoo.get(zviera) < hodnota:
            print(kluc)


def vyber_lahsie(zviera):
    vys = {}
    for kluc, hodnota in sorted(zoo.items()):
        if zoo.get(zviera) > hodnota:
            vys[kluc] = hodnota
    return vys


tazsie_ako("zirafa")
print(vyber_lahsie('pyton'))
