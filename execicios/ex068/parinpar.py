from random import randint
print('-=' * 30)
print('Vamos jogar par ou impa!')
print('=-' * 30)
cont = 0
com = randint(0, 10)
res = ''
sta = ''
while True:
    cont += 1
    n = int(input('Digite um valor: '))
    p = str(input('Par ou Ípar [P/Í]: '))
    sta = 'Par' if n + com % 2 == 0 else 'Ípar'
    if (not p in 'IiPp') or n < 0:
        print('Opção invalida tente novamente')
        break
    if n + com % 2 == 0 and p in 'Pp' or n + com % 2 != 0 and p in 'Ii':
        res = 'VENCEL'
    else:
        res = 'PERDEU'
    print('--' * 30)
    print(f'O computador jogou {com} e Você jogou {n}, Total de {com + n} deu {sta}')
    print('--' * 30)
    print(f'Você {res}')
    if res == 'PERDEU':
        break
    print('Vamos jogar novamente....')
print(f'GAME OVER!, Vovê vencel {cont} vezes')
