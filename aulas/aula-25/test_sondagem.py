from sondagem import contar_votos, vencedor

def test_lista_vazia():
    assert contar_votos([]) == {}

def test_um_voto():
    assert contar_votos(["B"]) == {"B": 1}

def test_varios_votos():
    assert contar_votos(["A", "B", "A", "C"]) == {"A": 2, "B": 1, "C": 1}

def test_vencedor():
    assert vencedor({"A": 2, "B": 1, "C": 1}) == "A"