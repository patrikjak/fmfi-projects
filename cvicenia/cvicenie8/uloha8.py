def vzostupne(zoznam):
    for i in range(len(zoznam)):
        if zoznam[i] <= zoznam [i + 1]:
            return True
        else:
            return False


print(vzostupne([1, 5, 5, 8, 100]))
print(vzostupne(['pyton', 'python', 'pytliak']))
