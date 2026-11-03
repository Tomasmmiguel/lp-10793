from funcoes import dobro, e_par

def test_dobro():
    assert dobro(4) == 8
    assert dobro(0) == 0

def test_e_par():
    assert e_par(6) == True
    assert e_par(7) == False
    assert e_par(0) == True
