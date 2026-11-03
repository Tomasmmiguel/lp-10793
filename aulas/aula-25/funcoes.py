def dobro(n):
    return n * 2

def e_par(n):
    return n % 2 == 0

def preco_com_iva(preco):
    return round(preco * 1.23, 2)

def nota_final(teste, trabalho):
    return round(teste * 0.6 + trabalho * 0.4, 1)

def escalao(idade):
    if idade < 18:
        return "menor"
    return "maior"
