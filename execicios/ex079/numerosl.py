lista = []
n = 0
while True:
    #n = 0
    n = int(input('Digite um valor: '))
    if not n in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        r = str(input('Quer continuar?[S/N] ')).strip().lower()[0]
        if r in 'sn':
            break
    if r == 'n':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(lista)}')
