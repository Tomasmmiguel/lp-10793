def percentagens(contagem):
    total = sum(contagem.values())
    if total == 0:
        return {resposta: 0.0 for resposta in contagem}
    resultado = {}
    for resposta in contagem:
        resultado[resposta] = round(contagem[resposta] * 100 / total, 1)
    return resultado