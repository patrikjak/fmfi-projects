def len_v_jednom(retazec1, retazec2):
    return (set(retazec1) - set(retazec2)) | (set(retazec2) - set(retazec1))


mn = len_v_jednom('isiel macek do malaciek', 'sosovicku mlacit')
print(mn)
