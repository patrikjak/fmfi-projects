def rgb(r, g, b):
    assert isinstance(r, int), "chybny parameter r, nie je to cele cislo"
    assert 0 <= r <= 255, "chybny parameter r, cislo musi byt intervale <0, 255>"
    assert isinstance(g, int), "chybny parameter g, nie je to cele cislo"
    assert 0 <= g <= 255, "chybny parameter g, cislo musi byt intervale <0, 255>"
    assert isinstance(b, int), "chybny parameter b, nie je to cele cislo"
    assert 0 <= b <= 255, "chybny parameter b, cislo musi byt intervale <0, 255>"
    return f"#{r:02x}{g:02x}{b:02x}"


print(rgb(100, 150, 200))
