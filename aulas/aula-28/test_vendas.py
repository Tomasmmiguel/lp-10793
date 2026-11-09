from funcoes import nivel_vendas

def test_nivel_vendas():
    assert nivel_vendas(80) == "alto"
    assert nivel_vendas(49) == "baixo"
    assert nivel_vendas(50) == "alto"
    assert nivel_vendas(0) == "baixo"

# test_vendas.py .                                                                                                                       [100%]
# ============================================================= 1 passed in 0.03s =============================================================