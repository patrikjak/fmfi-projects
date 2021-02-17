def vyhod_medzeru(text):
    bez_medzier = ""
    for i in text:
        if i != " ":
            bez_medzier += i
    return bez_medzier


print(vyhod_medzeru("   1   "))
