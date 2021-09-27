n1 = int(input('Diga um numero: '))
n2 = int(input('Diga um numero: '))
n3 = int(input('Diga um numero: '))

maior = n1
soma = n2 + n3

if n2 > n1 and n2 > n3:
    maior = n2
    soma = n1 + n3
elif n3 > n1 and n3 > n2:
    maior = n3
    soma = n2 + n1

tri = ''
if n1 != n2 != n3 != n1:
    tri = 'Escaleno'
elif n1 == n2 == n3:
    tri = 'Equilátero'
else:
    tri = 'Isósceles'

print('\033[0;31m-=\033[m' * 30)
if maior >= soma:
    print('Você não pode fazer um triângulo')
else:
    print('Você pode forma um triângulo e ele será {}'.format(tri))
print('\033[32m-=\033[m' * 30)
