numer = str(input('Digite un numero ente 0 e 9999: '))

div = ('0' * (4 - len(numer)))+ numer

print('unidades', div[3])
print('dezenas', div[2])
print('centenas', div[1])
print('milhar', div[0])
