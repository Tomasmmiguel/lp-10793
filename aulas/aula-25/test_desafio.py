from desafio import desconto

def test_desconto():
    assert desconto(100, 10) == 90.0
    assert desconto(50, 0) == 50.0
    assert desconto(20, 50) == 10.0
    assert desconto(100, 100) == 0.0   