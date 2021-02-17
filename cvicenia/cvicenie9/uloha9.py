import tkinter
canvas = tkinter.Canvas()
canvas.pack()


def sort_y(zoznam):
    novy_zoznam = []
    for i in range(len(zoznam)):
        ntica = (zoznam[i][1], zoznam[i][0])
        novy_zoznam.append(ntica)
    novy_zoznam.sort()
    dlzka = len(novy_zoznam)
    zoznam.clear()
    for i in range(dlzka):
        dobra_ntica = (novy_zoznam[i][1], novy_zoznam[i][0])
        zoznam.append(dobra_ntica)
    return zoznam


xy = [(100, 30), (200, 10), (300, 20)]
dlzka = len(xy)
print(sort_y(xy))

for i in range(dlzka):
    zoznam = sort_y(xy)
    if i + 1 == dlzka:
        canvas.create_line(zoznam[i], zoznam[i])
    else:
        canvas.create_line(zoznam[i], zoznam[i+1])

canvas.mainloop()
