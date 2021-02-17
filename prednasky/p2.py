# for x in range(5):
#    print("Hello", x)
#    print("there")

# n = int(input("Zadaj pocet: "))
# y = 0
# for x in range(n):
#   y = y + x
# print(y)

# for x in "python", 123, 22/7, print, abs:
#    print("hodnota x je: ", x, "typu: ", type(x))

# str = input("Zadaj retazec: ")
# x = 0
# y = ""
# for znak in str:
#    #print(x, "znak: ", znak)
#    y = y + znak + "*"
#    x += 1
# print("dlzka retazca = ", x)
# print("y = ", y)

# n = int(input("Zadaj n: "))
# f = 1
# for i in range(2, n+1):
#    f *= i
# print(f"{i}! = {f}")

# for i in range(20, 30):
#    print(i, end=" ")

# for i in range(10, 1, -1):
#    print(i, end=" ")

# for i in reversed(range(2, 11)):
#    print(i, end=" ")

# for i in reversed("python"):
#    print(i, end=" ")

import math

for x in range(0, 360, 5):
    print("*" * int(math.sin(math.radians(x))*35+40))
    # print(f'{x:5} {s:8.3f} {y:8.3f}')
