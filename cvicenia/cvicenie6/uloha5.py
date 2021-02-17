def rozsekaj(text, sirka):
    if len(text) > sirka:
        rozsekany = ""
        pocitadlo = 0
        for i, znak in enumerate(text):
            rozsekany += znak
            pocitadlo += 1
            if pocitadlo == sirka:
                rozsekany += "\n"
                pocitadlo = 0
        print(rozsekany)
    else:
        print(text)


rozsekaj("Anicka dusicka, kde si bolaa", 10)
    