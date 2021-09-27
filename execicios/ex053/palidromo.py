frase = str(input('Digite uma frase para análise: ')).strip().lower()
frase2 = frase.split()
frase = ''.join(frase2)
fraseInversa = ''
for c in range(0, len(frase)):
    fraseInversa += frase[- (c + 1)]
if fraseInversa == frase:
    print('\033[33mÉ um palindromo')
else:
    print('Não é um palindromo')
"""
o for pode ser subistituido por 
inverso = frase2[::-1]

"""
