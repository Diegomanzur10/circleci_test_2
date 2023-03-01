from code.main import suma, resta, multiplicacion, division, modulo
import pytest

@pytest.mark.parametrize(
    (       ## Set de variables de la funcion
        "a",
        "b",
        "valor_esperado",
    ),
    [
        (1,
         1,
         2,),

        (1,
         2,
         3,),

        (1,
         3,
         4,),

        (1,
         4,
         5,),
    ],

    ids=[
        "suma_1_1",
        "suma_1_2",
        "suma_1_3",
        "suma_1_4",
    ]
)
def test_suma(a, b, valor_esperado):
    assert suma(a,b) == valor_esperado

@pytest.mark.skip(reason = "Funcion a depricar")
def test_division():
    assert division(1, 1) == 1

def test_modulo():
    assert modulo(10, 2) == 0

