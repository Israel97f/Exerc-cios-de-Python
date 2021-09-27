dicionario = dict()
lista = list()
s = 0
media = 0
while True:
    dicionario['Nome'] = str(input('Nome: ')).strip()
    while True:
        dicionario['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if dicionario['sexo'] in 'FM':
            break
        else:
            print('Opção invalida porfavor temte novamente!')
    dicionario['idade'] = int(input('Idade: '))
    lista.append(dicionario.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if r in 'sn':
            break
    if r in 'n':
        break
for i in range(0, len(lista)):
    s += lista[i]['idade']
media = s / len(lista)
print('-=' * 30)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram:', end=' ')
for v in lista:
    if v['sexo'] == 'F':
        print(f'{v["Nome"]}', end=' ')
print(f'\n- Lista das pesoas que estão acima da média: \n')
for v in lista:
    if v['idade'] > media:
        print(f'Nome = {v["Nome"]}; Sexo = {v["sexo"]}; Idade = {v["idade"]}')
        print()
print('<< ENCERADO >>')
