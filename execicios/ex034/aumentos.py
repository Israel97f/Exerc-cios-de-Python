sal = int(input('Diga o seu salario '))

if sal <= 1250:
    print('O seu salario esta no limite de R$ 1250.00 então seu novo salario é R${:.2f}'.format(sal + sal * 0.15))
else:
    print('O seu salario esta fora do limite de R$ 1250.00 então seu novo salario é R${:.2f}'.format(sal + sal * 0.10))
