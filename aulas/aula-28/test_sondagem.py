from sondagem import percentagens

def test_percentagens():
    contagem = {"Telemóvel": 12, "Auscultadores": 5, "Conversa": 2, "Pressa": 1}
    assert percentagens(contagem) == {
        "Telemóvel": 60.0,
        "Auscultadores": 25.0,
        "Conversa": 10.0,
        "Pressa": 5.0,
    }