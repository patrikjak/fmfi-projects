def rozdel(mnozina):
    m1, m2 = set(), set()
    for i in mnozina:
        if isinstance(i, int) or isinstance(i, float):
            m1.add(i)
        elif isinstance(i, str):
            m2.add(i)
    return m1, m2


m1, m2 = rozdel({7, 7.5, '12', 3, 'python'})
print(m1)
print(m2)
