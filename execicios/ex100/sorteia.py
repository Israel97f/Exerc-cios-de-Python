from random import randint
from time import sleep
números = list()
def sorteia(lista):
    print('Sorteando 5 valores para a lista')
    for i in range(0, 5, 1):
        n = randint(1, 60)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'somando os valores pares de {números} temos {soma}') 
    

# Programa Principl
sorteia(números)
somaPar(números)
