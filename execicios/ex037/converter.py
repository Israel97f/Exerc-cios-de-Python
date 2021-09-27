valor = int(input('\033[32mdigite um numero inteiro:  \033[m'))
print("""\033[33mEscolha a opção de converção
[1] binário
[2] octal
[3] hexadecimal\033[m""")
n = int(input('Digite sua opção: '))

cor = {'lin':'\033[m','red': '\033[31m','gre':'\033[32m','yel':'\033[33m', 'blu':'\033[34m'}
print('{}-={}'.format(cor['blu'],cor['lin']) * 30)
if n == 1:
    print('O número convertido para BINARIO é {}'.format(bin(valor)[2:]))
elif n == 2:
    print('O nu número comvertido para OCTAL é {}'.format(oct(valor)[2:]))
elif n == 3:
    print('O número comvertido para HEXADECIMAL é {}'.format(hex(valor)[2:]))
else:
    print('{}O numero digitado não é uma opição valida{}'.format(cor['red'], cor['lin']))
print('{}-={}'.format(cor['gre'],cor['lin']) * 30)
