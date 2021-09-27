#import os
#os.system('cls')
lista = []
r = ''
n = 0
i = 0
while True:
    i += 1
    n = int(input('Digite um valor: '))
    lista.append(n)
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if r in 'sn':
            break
    if r in 'n':
        break
print('-=' * 30)
print(f'Foram digitados {i} números')
print(f'Os valores em ordem decrecente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi encontrado na lista!')
