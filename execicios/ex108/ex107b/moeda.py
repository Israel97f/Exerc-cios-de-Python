def aumentar(p, por=0):
    return p * (1 + por/100)


def diminuir(p, por=0):
    return p * (1 - por/100)


def metade(p):
    return p / 2


def dobro(p):
    return p * 2


def moeda(valor):
    return f'R${valor:.2f}'
    