# sifra = {
#     'a': 'b',
#     'b': 'c',
#     'c': 'd',
#     'd': 'e',
#     'e': 'f',
#     'f': 'g',
#     'g': 'h',
#     'h': 'i',
#     'i': 'j',
#     'j': 'k',
#     'k': 'l',
#     'l': 'm',
#     'm': 'n',
#     'n': 'o',
#     'o': 'p',
#     'p': 'q',
#     'q': 'r',
#     'r': 's',
#     's': 't',
#     't': 'u',
#     'u': 'v',
#     'v': 'w',
#     'w': 'x',
#     'x': 'y',
#     'y': 'z',
#     'z': 'a'
# }
#
#
# def zasifruj(sifra, text):
#     vys = []
#     for i in range(len(text)):
#         if text[i] == " ":
#             vys.append(" ")
#         else:
#             vys.append(sifra.get(text[i]))
#     return " ".join(vys)
#
#
# def desifruj(sifra, text):
#     vys = []
#     for i in range(len(text)):
#         for kluc, hodnota in sifra.items():
#             if text[i] == " ":
#                 vys.append(" ")
#                 break
#             elif text[i] == hodnota:
#                 vys.append(kluc)
#     return "".join(vys)
#
#
# t = zasifruj(sifra, "programovanie v pythone je cool")
# print(t)
# print(desifruj(sifra, t))

print((2+3)*(5-2)**(6//3)**(17 % 7)*14//11)
print((2+3)*(5-2), ((2).__add__(3)).__mul__((5).__sub__(2)))
print((2+3)*(5-2)**(6//3), ((2).__add__(3)).__mul__((5).__sub__(2).__pow__((6).__floordiv__(3))) )
print((2+3)*(5-2)**(6//3)**(17 % 7), ((2).__add__(3)).__mul__((5).__sub__(2).__pow__(((6).__floordiv__(3)).__pow__((17).__mod__(7)))))
print((2+3)*(5-2)**(6//3)**(17 % 7)*14//11, ((2).__add__(3)).__mul__((5).__sub__(2).__pow__(((6).__floordiv__(3)).__pow__(((17).__mod__(7)).__mul__(14).__floordiv__(11)))) )
