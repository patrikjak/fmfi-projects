# 6. zadanie: logo
# autor: Patrik Jakab
# datum: 13.11.2020

def preloz(meno_suboru, tab=4):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    riadok = subor.readline()
    arr, prikazy, vsetky_prikazy_riadky, vsetky_prikazy = [], [], [], []
    subor_py = open(meno_suboru.replace(".txt", ".py"), 'w', encoding="utf-8")
    subor_py.write("import turtle\n")
    subor_py.write("t = turtle.Turtle()\n")
    while riadok != "":
        arr.append(riadok)
        riadok = subor.readline()
    for i in range(len(arr)):
        if arr[i].count('[') > -1:
            arr[i] = arr[i].replace('[', ' [ ')
            arr[i] = arr[i].replace(']', ' ] ')
        prikaz_riadok = arr[i].split()
        prikazy.append(" ".join(prikaz_riadok))
    for i in range(len(prikazy)):
        prikaz = prikazy[i].split()
        vsetky_prikazy_riadky.append(prikaz)
    param, cycle, opakovania = 0, 0, 0
    for i in range(len(vsetky_prikazy_riadky)):
        for j in range(len(vsetky_prikazy_riadky[i])):
            prik = vsetky_prikazy_riadky[i][j]
            vsetky_prikazy.append(prik)
            if prik != "pu" and prik != "pd" and prik != "repeat" and prik != "[" and prik != "]":
                if param == 0:
                    if prik == "setpc":
                        prik = "pencolor"
                    if prik == "setpw":
                        prik = "pensize"
                    if opakovania == 1:
                        subor_py.write(f"{prik}):\n")
                        opakovania = 0
                    else:
                        if cycle >= 1:
                            subor_py.write(" " * (tab * cycle))
                        subor_py.write(f"t.{prik}(")
                        param = 1
                else:
                    subor_py.write(f"{prik})\n")
                    param = 0
            elif prik == "pu" or prik == "pd":
                if cycle >= 1:
                    subor_py.write(" " * (tab * cycle))
                subor_py.write(f"t.{prik}()\n")
            elif prik == "repeat":
                if cycle >= 1:
                    subor_py.write(" " * (tab * cycle))
                subor_py.write("for _ in range(")
                cycle += 1
                opakovania = 1
            elif prik == "]":
                cycle -= 1
    subor_py.write("turtle.mainloop()")
    subor.close()
    subor_py.close()
#     print(vsetky_prikazy)
#
#
# preloz('subory/projekt6/subor8.txt')
