def riadky_s_textom(meno_suboru, text):
    subor = open(meno_suboru, 'r', encoding="utf-8")
    riadok = subor.readline()
    while riadok != "":
        if riadok.find(text) > -1:
            print(end=riadok)
        riadok = subor.readline()
    subor.close()


riadky_s_textom('subory/text3.txt', 'ali')
print("\n")
riadky_s_textom('uloha9.py', 'if')
