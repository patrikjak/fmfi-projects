def start(zoznam, n):
    new_list = []
    for i in range(len(zoznam)):
        new_list.append(zoznam[i][:n])
    return new_list


mesiace = ['januar', 'februar', 'marec', 'april', 'maj',
           'jun', 'jul', 'august', 'september',
           'oktober', 'november', 'december']

print(start(mesiace, 3))
