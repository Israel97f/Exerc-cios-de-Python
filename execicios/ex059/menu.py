op = 0
res = 0
while op != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    print('-------- Menu --------')
    print("""\033[33m
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SARIR DO PROGRAMA\033[m""")
    op = int(input('Opção: '))
    if op == 1:
        res = n1 + n2
    elif op == 2:
        res = n1 * n2
    elif op == 3:
        if n1 > n2:
            res = n1
        elif n2 > n1:
            res = n2
        else:
           print('Os valores são iguais') 
    elif op == 4:
        res = 0
    else:
        if op != 5:
            print('\033[31mOpção invalida tente novamente!\033[m')
    if op == 1 or op == 2 or op == 3 and n1 != n2:
        print('O resutado é {}'.format(res))
