zoz = ['prvy', 'druhy', 'treti', 'stvrty', 'piaty']


def najdlhsie(zoznam):
    max_num = 0
    max_item = ""
    for i in range(len(zoznam)):
        if len(zoznam[i]) > max_num:
            max_item = zoznam[i]
            max_num = len(zoznam[i])
    return max_item


print(najdlhsie(zoz))