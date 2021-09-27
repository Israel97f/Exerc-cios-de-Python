print('\033[32m==' * 30)
print('\033[33m{:^60}'.format('LOJA BARATÃO'))
print('\033[32m==\033[m' * 30)
s = menor = cont = i = 0
nmer = ''
while True:
    n = str(input('Nome do Produto: ')).upper().strip()
    p = float(input('Preço R$: '))
    cont += 1
    s += p
    if cont <= 1 or p < menor:
        menor = p
        nmer = n
    """else:
        if p < menor:
            menor = p
            nmer = n"""
    if p > 1000:
        i += 1
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'SN':
            break
    if c == 'N':
        break
print('==' * 30)
print('{:^60}'.format('FIM DO PROGRAMA'))
print('==' * 30)
print("""
O total da compra foi R$ {:.2f}
Temos {} produtos custando mais de R$ 1000.00
O produto mais barata foi {} que custa {:.2f}""".format(s, i, nmer, menor))
