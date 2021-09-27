n1 = int(input('Diga um numero: '))
n2 = int(input('Diga um numero: '))
n3 = int(input('Diga um numero: '))
'''
if n1 > n2:
    if n2 > n3:
        if n1 < (n2 + n3):
            print('Você pode formar um triângulo')
        else:
            print('Você não pode formar um triângulo')
    else:
        if n1 > n3:
            if n1 < (n2 + n3):
                print('Você pode formar um triângulo')
            else:
                print('Você não pode formar um triângulo')
        else:
            if n3 < (n1 + n2):
                print('Você pode formar um triângulo')
            else:
                print('Você não pode formar um triângulo')
else:
    if n1 > n3:
        if n2 < (n1 + n3):
            print('Você pode formar um triângulo')
        else:
            print('Você não pode formar um triângulo')
    else:
        if n2 > n3:
            if n2 < (n1 + n3):
                print('Você pode formar um triângulo')
            else:
                print('Você não pode formar um triângulo')
        else:
            if n3 < (n2 + n1):
                print('Você pode formar um triângulo')
            else:
                print('Você não pode formar um triângulo')
'''

maior = n1
soma = n2 + n3

if n2 > n1 and n2 > n3:
    maior = n2
    soma = n1 + n3
if n3 > n1 and n3 > n2:
    maior = n3
    soma = n2 + n1
print('\033[0;31m-=\033[m' * 30)
if maior >= soma:
    print('Você não pode fazer um triângulo')
else:
    print('Você pode forma um triângulo')
print('\033[32m-=\033[m' * 30)