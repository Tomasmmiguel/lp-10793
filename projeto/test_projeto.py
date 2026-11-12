from funcoes import percentagem

def test_percentagem():
    assert percentagem(50, 200) == 25.0
    assert percentagem(0, 100) == 0.0
    assert percentagem(5, 0) == 0.0
    print("Os testes passaram")


# Mais um teste, para outra função do teu projeto.
from funcoes import percentagem, mais_frequente

def test_mais_frequente():
    assert mais_frequente({"Velocidade": 30, "Álcool": 10}) == "Velocidade"
    assert mais_frequente({"B": 5, "A": 5}) == "A"
    assert mais_frequente({}) is None