val = int(input('Diga o valor da casa: '))
sal = int(input('Qual o seu salario? '))
yar = int(input('Em quantos anos pretende pagar? '))

cor = {'lin':'\033[m','red': '\033[31m','gre':'\033[32m','yel':'\033[33m', 'blu':'\033[34m'}

par = val / (yar * 12)
print('{}-={}'.format(cor['blu'], cor['lin']) * 25)
if sal * 0.3 > par:
    print('{}Seu enprestimo foi aprovaado{}'.format(cor['gre'], cor['lin']))
else:
    print('{}Lamento mas você não pode finaciar essa casa{}'.format(cor['red'], cor['lin']))
print('{}-={}'.format(cor['blu'], cor['lin']) * 25)
