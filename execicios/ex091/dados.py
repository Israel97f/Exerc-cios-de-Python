from random import randint
dicionario = dict()
rank = dict()
maior = 0
index = ''
cont = 0
for i in range(0, 4):
    n = str(i + 1)
    dicionario['jogador' + n] = randint(1, 6)
print('Valores sorteados:')
print()
for c, v in dicionario.items():
    print(f'O {c} tirou {v}')
while True:
    for k, v in dicionario.items():
        if v > maior:
            maior = v
            index = k
    rank[index] = maior
    del dicionario[index]
    maior = 0
    index = ''
    if len(rank) == 4:
        break  
print(f'{" Ranking dos jogadores ":=^60}')
for k, v in rank.items():
    cont += 1
    print(f'{cont}° lugar {k} com {v}')
