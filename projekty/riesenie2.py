# 2. zadanie: spirala
# autor: Patrik Jakab
# datum: 05.10.2020

import tkinter
canvas = tkinter.Canvas()
canvas.pack()

startova_dlzka = int(input("Zadaj startovaciu dlzku: "))
inkrement = int(input("Zadaj inkrement: "))
sucet_dlzok = int(input("Zadaj sucet dlzok: "))

x, y = 150, 150
smer = "u"
aktualna_dlzka, sucet = 0, 0

while sucet < sucet_dlzok:
    if smer == "u":
        if aktualna_dlzka != 0:
            aktualna_dlzka += inkrement
            sucet += aktualna_dlzka
            if sucet >= sucet_dlzok:
                canvas.create_line(x, y, x - (sucet_dlzok - (sucet - aktualna_dlzka)) * (1/(2**0.5)), y - (sucet_dlzok - (sucet - aktualna_dlzka)) * (1/(2**0.5)))
                break
            canvas.create_line(x, y, x - aktualna_dlzka * (1/(2**0.5)), y - aktualna_dlzka * (1/(2**0.5)))
            y -= aktualna_dlzka * (1/(2**0.5))
            x -= aktualna_dlzka * (1/(2**0.5))
            smer = "l"
        else:
            if startova_dlzka > sucet_dlzok:
                canvas.create_line(x, y, x - sucet_dlzok * (1/(2**0.5)), y - sucet_dlzok * (1/(2**0.5)))
                break
            canvas.create_line(x, y, x - startova_dlzka * (1/(2**0.5)), y - startova_dlzka * (1/(2**0.5)))
            y -= startova_dlzka * (1/(2**0.5))
            x -= startova_dlzka * (1/(2**0.5))
            aktualna_dlzka += startova_dlzka
            sucet += aktualna_dlzka
            smer = "l"
    if smer == "l":
        aktualna_dlzka += inkrement
        sucet += aktualna_dlzka
        if sucet >= sucet_dlzok:
            canvas.create_line(x, y, x - (sucet_dlzok - (sucet - aktualna_dlzka)) * (1/(2**0.5)), y + (sucet_dlzok - (sucet - aktualna_dlzka)) * (1/(2**0.5)))
            break
        canvas.create_line(x, y, x - aktualna_dlzka * (1/(2**0.5)), y + aktualna_dlzka * (1/(2**0.5)))
        x -= aktualna_dlzka * (1/(2**0.5))
        y += aktualna_dlzka * (1/(2**0.5))
        smer = "d"
    if smer == "d":
        aktualna_dlzka += inkrement
        sucet += aktualna_dlzka
        if sucet >= sucet_dlzok:
            canvas.create_line(x, y, x + (sucet_dlzok - (sucet - aktualna_dlzka)) * (1/(2**0.5)), y + (sucet_dlzok - (sucet - aktualna_dlzka)) * (1/(2**0.5)))
            sucet = aktualna_dlzka
            break
        canvas.create_line(x, y, x + aktualna_dlzka * (1/(2**0.5)), y + aktualna_dlzka * (1/(2**0.5)))
        y += aktualna_dlzka * (1/(2**0.5))
        x += aktualna_dlzka * (1/(2**0.5))
        smer = "r"
    if smer == "r":
        aktualna_dlzka += inkrement
        sucet += aktualna_dlzka
        if sucet >= sucet_dlzok:
            canvas.create_line(x, y, x + (sucet_dlzok - (sucet - aktualna_dlzka)) * (1/(2**0.5)), y - (sucet_dlzok - (sucet - aktualna_dlzka)) * (1/(2**0.5)))
            break
        canvas.create_line(x, y, x + aktualna_dlzka * (1/(2**0.5)), y - aktualna_dlzka * (1/(2**0.5)))
        x += aktualna_dlzka * (1/(2**0.5))
        y -= aktualna_dlzka * (1/(2**0.5))
        smer = "u"

# while sucet < sucet_dlzok:
#     if smer == "u":
#         if aktualna_dlzka != 0:
#             aktualna_dlzka += inkrement
#             sucet += aktualna_dlzka
#             if sucet >= sucet_dlzok:
#                 canvas.create_line(x, y, x, y - (sucet_dlzok - (sucet - aktualna_dlzka)))
#                 break
#             canvas.create_line(x, y, x, y - aktualna_dlzka)
#             y -= aktualna_dlzka
#             smer = "l"
#         else:
#             if startova_dlzka > sucet_dlzok:
#                 canvas.create_line(x, y, x, y - sucet_dlzok)
#                 break
#             canvas.create_line(x, y, x, y - startova_dlzka)
#             y -= startova_dlzka
#             aktualna_dlzka += startova_dlzka
#             sucet += aktualna_dlzka
#             smer = "l"
#     if smer == "l":
#         aktualna_dlzka += inkrement
#         sucet += aktualna_dlzka
#         if sucet >= sucet_dlzok:
#             canvas.create_line(x, y, x - (sucet_dlzok - (sucet - aktualna_dlzka)), y)
#             break
#         canvas.create_line(x, y, x - aktualna_dlzka, y)
#         x -= aktualna_dlzka
#         smer = "d"
#     if smer == "d":
#         aktualna_dlzka += inkrement
#         sucet += aktualna_dlzka
#         if sucet >= sucet_dlzok:
#             canvas.create_line(x, y, x, y + (sucet_dlzok - (sucet - aktualna_dlzka)))
#             break
#         canvas.create_line(x, y, x, y + aktualna_dlzka)
#         y += aktualna_dlzka
#         smer = "r"
#     if smer == "r":
#         aktualna_dlzka += inkrement
#         sucet += aktualna_dlzka
#         if sucet >= sucet_dlzok:
#             canvas.create_line(x, y, x + (sucet_dlzok - (sucet - aktualna_dlzka)), y)
#             break
#         canvas.create_line(x, y, x + aktualna_dlzka, y)
#         x += aktualna_dlzka
#         smer = "u"

canvas.mainloop()