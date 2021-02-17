def rozdel(retazec):
    nove_retazce = []
    slovo = ""
    for i in range(len(retazec)):
        if retazec[i] != " " and retazec[i] != "\n":
            slovo += retazec[i]
            if i+2 <= len(retazec):
                if retazec[i+1] == " " or retazec[i+1] == "\n":
                    nove_retazce.append(slovo)
                    slovo = ""
            else:
                nove_retazce.append(slovo)
    return nove_retazce


print(rozdel("  jeden   dva tri"))
print(rozdel('ah\noj\n'))
cisla = input("Zadaj cisla: ")
print(rozdel(cisla))