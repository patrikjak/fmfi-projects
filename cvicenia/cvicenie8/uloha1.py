den = ['pondelok', 'utorok', 'streda', 'stvrtok', 'piatok', 'sobota', 'nedela']
day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
for i in range(len(day)):
    print(day[i], end=' ')
print()
for i in range(len(day)):
    print(den[i], end=' ')
print("\n")
for i in range(len(day)):
    print(den[i] + ' ', end=day[i])
    print()