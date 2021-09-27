n1 = int(input('Diga um numero: '))
n2 = int(input('Diga um numero: '))
n3 = int(input('Diga um numero: '))
'''
if n1 > n2:
    if n2 > n3:
        print('O maior é {} e o menor é {}'.format(n1, n3))
    else:
        if n1 > n3:
            print('O maior é {} e o menor é {}'.format(n1, n2))
        else:
            print('O maior é {} e o menor é {}'.format(n3, n2))
else:
    if n1 > n3:
        print('O maior é {} e o menor é {}'.format(n2, n3))
    else:
        if n2 > n3:
            print('O maior é {} e o menor é {}'.format(n2, n1))
        else:
            print('O maior é {} e o menor é {}'.format(n3, n1))
'''
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2 
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n1 > n2:
    maior = n3

print('O maior é {} e o menor é {}'.format(maior, menor))
