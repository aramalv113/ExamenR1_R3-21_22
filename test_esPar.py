from main import esPar
import pytest

data = [
    (2,True), # mes par
    (5,False), # mes impar
    ('a',None), # mes no numérico
    (2.3,True), # mes par flotante
    (7.2,False), # mes impar flotante
    (-2,False), # mes par negativo
    (-3,False) # mes impar negativo
]

@pytest.mark.parametrize("mes,resultado",data)
def test_eval(mes,resultado):
    assert esPar(mes) == resultado