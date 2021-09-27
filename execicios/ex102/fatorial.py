def fatorial(n, show=False):
    """-> Calcula o fatorial de um numero
    n: é o numero do fatorial a ser calculado
    show: é um parameto que mostra o calculo do fatorial
    retorno: retorta o fatorial de um numero
    """
    p = 1
    pr = ''
    for i in range(n, 0, -1):
        p *= i
    if show == False:
        return p
    else:
        for i in range(n , 0, -1):
            if i > 1:
                pr += f'{i} x '
            else:
                pr += f'{i} = {p}'
        return pr 


#Programa Principal
nun = int(input('Digite um numero: '))
print(fatorial(nun, True))
help(fatorial)
