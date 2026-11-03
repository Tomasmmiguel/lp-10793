from funcoes import preco_com_iva

def test_preco_com_iva():
    assert preco_com_iva(10) == 12.0
    assert preco_com_iva(100) == 123.0
    assert preco_com_iva(0) == 0.0
