import math

op = float(input('Qual o comprimento do cateto oposto '))

ad = float(input('Qual o comprimento do cateto adjacente '))

hi = math.sqrt(op ** 2 + ad ** 2)

print('A hipotenusa é {}'.format(hi))
