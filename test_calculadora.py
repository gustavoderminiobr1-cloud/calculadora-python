from calculadora import somar, subtrair, multiplicar


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(5, 3) == 2


def test_multiplicar():
    assert multiplicar(4, 3) == 12
