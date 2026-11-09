def nivel_vendas(quantidade):
    if quantidade >= 50:
        return "alto"
    return "baixo"

def percentagem(parte, total):
    return round(parte * 100 / total, 1)
