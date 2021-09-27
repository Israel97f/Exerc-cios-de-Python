def aumentar(p, por=0, monetario=False):
    if monetario == False:
        return p * (1 + por/100)
    else:
        return moeda(p * (1 + por/100))


def diminuir(p, por=0, monetario=False):
    if monetario == False:
        return p * (1 - por/100)
    else:
        return moeda(p * (1 - por/100))


def metade(p, monetario=True):
    if monetario == False:
        return p / 2
    else:
        return moeda(p / 2)


def dobro(p, monetario=False):
    if monetario == False:
        return p * 2
    else:
        return moeda(p * 2)


def moeda(valor):
    return f'R${valor:.2f}'
    