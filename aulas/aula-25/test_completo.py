from funcoes import nota_final, escalao

def test_nota_final():
    assert nota_final(10, 20) == 14.0
    assert nota_final(0, 0) == 0.0
    assert nota_final(20, 20) == 20.0

def test_escalao():
    assert escalao(10) == "menor"
    assert escalao(18) == "maior"
    assert escalao(40) == "maior"

from funcoes import dobro, e_par

def test_dobro_negativo():
    assert dobro(-3) == -6

def test_e_par_grande():
    assert e_par(1000000) == True
