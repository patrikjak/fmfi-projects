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
sucet = 0
for kluc, hodnota in sorted(zoo.items()):
    print(kluc, hodnota)
    sucet += hodnota
print("Priemerna hmotnost je:", sucet/len(zoo))
