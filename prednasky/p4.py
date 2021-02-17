# body = int(input("Zadaj body: "))
# if body == 90:
#     print("A")
# else:
#     if body >= 80:
#         print("B")
#     else:
#         if body >= 70:
#             print("C")
#         else:
#             if body >= 60:
#                 print("D")
#             else:
#                 if body >= 50:
#                     print("E")
#     print("Fx")


# bodiky = int(input("Zadaj body: "))
# if bodiky >= 90:
#     print("A")
# elif 80 <= bodiky < 90:
#     print("B")
# elif 70 <= bodiky < 80:
#     print("C")
# elif 60 <= bodiky < 70:
#     print("D")
# elif 50 <= bodiky < 60:
#     print("E")
# else:
#     print("Fx")

import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

# for i in range(100):
#     x = random.randint(0, 300)
#     y = random.randint(0, 300)
#     a = random.randint(3, 30)
#     if  a <= 10:
#         farba = "red"
#     elif a <= 20:
#         farba = "blue"
#     else:
#         farba = ""
#     canvas.create_rectangle(x, y, x+a, y+a, fill=farba)

# for i in range(1000):
#     x = random.randint(0, 300)
#     y = random.randint(0, 300)
#     if  random.randrange(6):
#         farba = "red"
#     else:
#         farba = "green"
#     canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba, width=0)

# cislo = int(input("? "))
# pocet = 0
# for delitel in range(1, cislo+1):
#     if cislo % delitel == 0:
#         pocet += 1
#         if pocet > 2:
#             # ... uz netreba ist dalej, pre zistenie ci to je prvocislo
#             break
#         print(delitel, end=" ")
# if pocet == 2:
#     print(cislo, 'je prvocislo')
# else:
#     print(cislo, "nie je prvocislo")
# print("Pocet delitelov je: ", pocet)
#
# ciselko = int(input("Zadaj cislo na test: "))
# for delitel in range(2, cislo):
#     if cislo % delitel == 0:
#         break
#
# if cislo > 1 and (ciselko==2 or delitel == ciselko-1):
#     print(ciselko, "je prvocislo")
# else:
#     print(ciselko, "nie je prvocislo")
#
# j = 0
# while j < 1:
#     print(j)
#     j += .1

# cislo = float(input('zadaj číslo:'))
#
# x = 1
# while x**2 < cislo:
#     x += 0.001
#
# print('odmocnina', cislo, 'je', x)

cislo = float(input('zadaj číslo:'))

od = 1
do = cislo

x = (od + do) / 2

pocet = 0
while abs(x**2 - cislo) > 0.001:
    if x**2 > cislo:
        do = x
    else:
        od = x
    x = (od + do) / 2
    pocet += 1

print('druhá odmocnina', cislo, 'je', x)
print('počet prechodov while-cyklom bol', pocet)

# canvas.mainloop()