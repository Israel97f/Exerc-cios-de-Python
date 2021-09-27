n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite o últmo número: '))
i = pos = tr = 0
par = ''
tupla = (n1, n2, n3, n4)
for c in tupla:
    if c == 9:
        i += 1
    if c == 3:
        pos = tupla.index(3)
        tr = c
    if c % 2 == 0:
        par += str(c) + ' '
print(f'\033[33mVocê digitou os valores {tupla}')
print(f'O valor 9 apareceu {i} vezes') # ou print(f'O valor 9 apareceu {tupla.cont(9)} vezes')
if tr == 3:
    print(f'O valor 3 foi digitado na posição  {pos}')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {par}')
