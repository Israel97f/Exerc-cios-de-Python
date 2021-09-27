n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

cor = {'lin':'\033[m','red': '\033[31m','gre':'\033[32m','yel':'\033[33m', 'blu':'\033[34m'}

print('{}-={}'.format(cor['blu'], cor['lin']) * 20)
if n1 > n2:
    print('{}O primeiro valor é maior{}'.format(cor['gre'], cor['lin']))
elif n1 < n2:
    print('{}O segundo valor é o maior{}'.format(cor['yel'], cor['lin']))
else:
    print('Não existe valor maior')
print('{}-={}'.format(cor['blu'], cor['lin']) * 20)