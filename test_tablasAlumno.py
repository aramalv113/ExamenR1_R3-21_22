from main import tablas_alumno
import pytest

data = [
    (6,12,(2,4)), # rango [6-8] mes par
    (8,3,(1,3,5)), # rango [6-8] mes impar
    (9,2,(6,8,10)), # rango (8-10] mes par
    (9,1,(7,9)), # rango (8-10] mes impar
    (11,4,(11,12,13)), # rango (10,12] mes par
    (11,6,(11,12,13)), # rango (10,12] mes impar
    (11.2,6.43,(11,12,13)), # valores flotantes
    ('a',2,None), # uno de los parámetros es no numérico
]

@pytest.mark.parametrize("edad,mes,rango",data)
def test_eval (edad,mes,rango):
    assert tablas_alumno(edad,mes) == rango,"Fallo"