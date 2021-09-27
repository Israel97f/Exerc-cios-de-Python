lista = []
for c in range(0, 5):
    n = int(input(f'Digite um valor par a posiçâo {c}: '))
    lista.append(n)
print('==' * 30)
print(f'\033[33mVocê digitou o vs valores {lista}\033[m')
print(f'O maior valor digitado foi {max(lista)} nas posições', end=' ')
for c, v in enumerate(lista):
    if max(lista) == v:
        print(f'{c:.<3}', end=' ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições', end=' ')
for c, v in enumerate(lista):
    if min(lista) == v:
        print(f'{c:.<3}', end=' ')
        