# 1. zadanie: retazec
# autor: Patrik Jakab
# datum: 09.10.2020

str = input('?')
dlzka = 0
rev_str = ""
for i in str:
    dlzka += 1
for i in reversed(str):
    rev_str += i

print('dlzka =', dlzka)
print('prevrat =', rev_str)
for j in range(dlzka):
    for i in str:
        print(i, end=" * ")
    print()
    for k in rev_str:
        print("* ", end=k)
        print(end=" ")
    print()