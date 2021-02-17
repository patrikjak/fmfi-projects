recept = ['cukor', 100, 'g', 'vajíčka', 5, 'ks', 'mlieko', 2, 'dcl']


def vypis_recept(list):
    j = 0
    for i in range(int(len(list) / 3)):
        print(list[j], list[j+1], list[j+2])
        j += 3


vypis_recept(recept)