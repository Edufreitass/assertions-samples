import pytest


def funcao_que_levanta_excecao():
    raise ValueError("Um erro!")


def test_excecao():
    with pytest.raises(ValueError):
        funcao_que_levanta_excecao()
