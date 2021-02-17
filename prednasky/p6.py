macek = """Išiel macek do malacek
šošovičku mlácic"""
print(macek)

print("nt" in "Monty")
print("tyP" in "Monty Python")

abc = "Monty Python"
print(abc[6])
abc[-1] == abc[len(abc)-1]
print(abc[-5])

a = "Python"
for i in range(-1, -len(a)-1, -1):
    print(i, a[i])

b = "Monty Python"
print(b[6:11])
print(b[6:12])
print(b[6:len(b)])
print(b[10:16])

c = "Python"
for i in range(len(c)):
    print(f'{i}:{i+3} {a[i:i+3]}')

for i in range(len(c)):
    print(f'{i}:{len(c)} {a[i:len(c)]}')

print(c[1:-1][1:-1])

