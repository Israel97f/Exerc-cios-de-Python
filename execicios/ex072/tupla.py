num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um numero entre 0 é 20: '))
    if 0 <= n <=20:
        break
    else:
        print('Opição invalida por favor tente novamene.', end=' ')
print(f'\033[35mVocê digitou o número {num[n]}')