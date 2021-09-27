n = 0
lista = []
impa = []
par = []
r = ''
while True:
    n = int(input('Dingite um valor: '))
    lista.append(n)
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if r in 'sn':
            break
    if r in 'n':
        break
for c in lista:
    if c % 2 ==0:
        par.append(c)
    else:
        impa.append(c)
print('\033[36m==' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impa}')
