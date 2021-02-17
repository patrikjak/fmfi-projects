def vyhod_none(ntica):
    nova_ntica = ()
    for prvok in ntica:
        if prvok is not None:
            nova_ntica = nova_ntica + (prvok,)
    return nova_ntica


print(vyhod_none((None, 1, None, None, 2, None, 3)))
