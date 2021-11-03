from main import comprueba_edad_y_mes
import pytest

data = [
    (8,12,0), # edad y mes correctos
    (-2,6,1), # edad incorrecta
    (8,13,-1), # mes incorrecto
    (1,2,1), # ambos datos incorrectos
    ('a',6,None), # algún dato no numérico
    (8.2,12.4,0) # datos flotantes
]

@pytest.mark.parametrize("edad,mes,resultado",data)
def test_eval (edad,mes,resultado):
    assert comprueba_edad_y_mes(edad,mes) == resultado