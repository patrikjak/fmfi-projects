def cele(zoznam):
    new_list = []
    for i in range(len(zoznam)):
        new_list.append(int(zoznam[i]))
    return new_list


print(cele(list(str(2**20))))
