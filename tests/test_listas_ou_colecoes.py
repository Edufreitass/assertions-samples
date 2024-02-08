def test_listas_iguais():
    assert [1, 2, 3] == [1, 2, 3]


def test_conjuntos_iguais():
    assert set([1, 2, 3, 2]) == set([3, 1, 2])
