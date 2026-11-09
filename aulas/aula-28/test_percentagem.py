from funcoes import percentagem

def test_percentagem():
 assert percentagem(50, 200) == 25.0
 assert percentagem(1, 3) == 33.3
 assert percentagem(0, 10) == 0.0