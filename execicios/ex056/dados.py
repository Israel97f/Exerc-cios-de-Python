mu = 0
ho = ''
me = 0
maior = 0
soma = 0
for c in range(0, 4):
    print('----------{}°----------'.format(c + 1))
    n = str(input('Digite seu nome: '))
    i = int(input('Digite sua idade: '))
    print("""Qual seu Sexo
    [1] Masculino
    [2] Feminino""")
    s = int(input('Opição: '))
    if s == 1 or s == 2:
        if i > maior and s == 1:
            maior = i
            ho = n
        if i <= 20 and s ==2:
            mu += 1
        soma += i
    else:
        print('\033[31mOpção invalida tente novamente')
        mu = -1
        ho = '-1'
        soma = -4
print('\033[35m-=' * 35)
print('O numero de mulheres com idade menor que 20 é {}'.format(mu))
print('O nome do homen mais velho é {}'.format(ho))
print('A media de idade das pessoas é {}'.format(soma / 4))