def prevrat(retazec):
    prevratene = ""     
    for i in range(len(retazec) -1, -1, -1):
        prevratene += retazec[i]
    print(prevratene)


prevrat("tseb eht si nohtyP")
