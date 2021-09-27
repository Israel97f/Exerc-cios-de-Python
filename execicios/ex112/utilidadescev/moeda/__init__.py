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
    return f'R${valor:.2f}'.replace('.', ',')
    

def resumo(valor, des=0, alm=0):
    print('-' * 30)
    print(f'{"Resumo do valor":^30}')
    print('-' * 30)
    print(f'Preço analizado:    {moeda(valor)}')
    print(f'O dobro do Preço:   {dobro(valor, True)}') # \t adiciona uma tabulação
    print(f'A metade do Preço:  {metade(valor, True)}')
    print(f'{des}% de desconto:    {diminuir(valor, des, True)}')
    print(f'{alm}% de almento:     {aumentar(valor, alm, True)}')
    print('-' * 30)
