def vencedor(contagem):
    melhor = None
    maior = 0
    for resposta in sorted(contagem):
        if contagem[resposta] > maior:
            melhor = resposta
            maior = contagem[resposta]
    return melhor
