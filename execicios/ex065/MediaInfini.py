i = 0
s = 0
n = 0
r = 's'
maior = 0
menor = 0
while r in 'Ss':
    n = int(input('Digite un número: '))
    r = str(input('\033[33mQuer continuar [S]:\033[m '))
    s += n
    i += 1
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n <  menor:
            menor = n 
print("""
A média é ......... {}
O maior número é .. {}
O menor numero é .. {}""".format(s / i, maior, menor ))
