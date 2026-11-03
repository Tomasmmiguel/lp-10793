def contar_votos(votos):
    contagem = {}
    for voto in votos:
        if voto in contagem:
            contagem[voto] = contagem[voto] + 1
        else:
            contagem[voto] = 1
    return contagem

def vencedor(contagem):
    return max(contagem, key=contagem.get)