import pytest


def test_valor_aproximado():
    assert (0.1 + 0.2) == pytest.approx(0.3)
