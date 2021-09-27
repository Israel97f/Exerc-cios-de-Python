dados = list()
maior = list()
menor = list()
count = 0

while True:
    count += 1
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if count == 1:
        maior.append(dados[:])
        menor.append(dados[:])
    if dados[1] >= maior[0][1] and count > 1:
        if dados[1] > maior[0][1]:
            maior.clear()
            maior.append(dados[:])
        else:
            maior.append(dados[:])
    if dados[1] <= menor[0][1] and count > 1:
        if dados[1] < menor[0][1]:
            menor.clear()
            menor.append(dados[:])
        else:
            menor.append(dados[:])
    dados.clear()
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if r in 'sn':
            break
    if r in 'n':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {count}')
print(f'O maior pesso foi {maior[0][1]}kg. Peso de', end=' ')
for c in range(0, len(maior)):
    print(f'[{maior[c][0]}]', end=' ')
print(f'\nO menor pesso foi {menor[0][1]}kg. Peso de', end=' ')
for c in range(0, len(menor)):
    print(f'[{menor[c][0]}]', end=' ')
