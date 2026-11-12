def percentagem(parte, total):
    if total == 0:
        return 0.0
    return parte * 100 / total


# Mais um teste, para outra função do teu projeto.
def mais_frequente(contagem):
    """Devolve a chave com o valor mais alto. Empate: a primeira por ordem alfabética. Vazio: None."""
    if not contagem:
        return None
    melhor = None
    for chave in sorted(contagem):
        if melhor is None or contagem[chave] > contagem[melhor]:
            melhor = chave
    return melhor