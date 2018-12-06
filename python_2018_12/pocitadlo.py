cisla = [1,2,3,4,4,1,2,7]


def kolik_cisla_mezi_cisly(hledane, cisla, verbose=True):
    """
    spocita 'hledane' cislo v seznamu 'cisla'
    a vrati kolik
    """
    kolik = 0
    for cislo in cisla:
        if cislo == hledane:
            kolik += 1
    if verbose:
        print("Cislo {0} je v seznamu cisel {1}krat.".format(hledane, kolik))
    return kolik


def postav_slovnik(cisla):
    vysledek = {}
    for cislo in cisla:
        vysledek[cislo] = kolik_cisla_mezi_cisly(cislo, cisla, verbose=False)
    return vysledek


def test_funkce():
    assert kolik_cisla_mezi_cisly(1, cisla) == 2
    assert kolik_cisla_mezi_cisly(20, cisla) == 0
    assert kolik_cisla_mezi_cisly(3, cisla) == 1


if __name__ == '__main__':
    test_funkce()
    print(postav_slovnik(cisla))
