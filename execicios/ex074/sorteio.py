from random import randint
n1 = n2 = n3 = n4 = n5 = maior = menor = i = 0
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
tupla = (n1, n2, n3, n4, n5)
for c in tupla:
    i += 1
    if i == 1:
        maior = c
        menor = c
    else:
        if c > maior:
            maoir = c
        if c < menor:
            menor = c

print(f'\033[33mOs valores sorteados foram: {tupla}')
print(f'O maior vlor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')



