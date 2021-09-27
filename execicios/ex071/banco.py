print('\033[33m==' * 30)
print('{:^60}'.format('BANCO DO \033[34mBRASIL'))
print('\033[33m==\033[m' * 30)

v = int(input('Que valor você quer sacar? R$'))

if v // 50 > 0:
    print('Total de {} cèdulas de R$ 50'.format(v // 50))
    v = v % 50
if v // 20 > 0:
    print('Total de {} cèdulas de R$ 20'.format(v // 20))
    v = v % 20
if v // 10 > 0:
    print('Total de {} cèdulas de R$ 10'.format(v // 10))
    v = v % 10
if v // 1 > 0:
    print('Total de {} cèdulas de R$ 1'.format(v // 1))
print('\033[33m==' * 30)
print('Volte sempre ao BANCO DO \033[34mBRASIL! Tenha um bom dia!\033[m')
b = input('Digite qualquer tecla  ')
