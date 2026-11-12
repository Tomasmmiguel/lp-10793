from sondagem import vencedor

def test_vencedor():
    assert vencedor({"Telemóvel": 12, "Pressa": 1}) == "Telemóvel"
    assert vencedor({"Pressa": 5, "Conversa": 5}) == "Conversa"
    assert vencedor({}) is None