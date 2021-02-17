def vyhod_duplikaty(retazec):
    retazec += " "
    novy_retazec = ""
    for i in range(len(retazec) - 1):
        if retazec[i] != retazec[i + 1]:
            novy_retazec += retazec[i]
    print(novy_retazec)


vyhod_duplikaty("Braatiiiislavaaa")
