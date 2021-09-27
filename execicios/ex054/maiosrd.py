from datetime import date
i = 0
yar = date.today().year
for c in range(0, 7):
    a = int(input('Digite um ano de nascimento: '))
    if yar - a < 21:
        i += 1
print('\033[33mDas 7 pessoas que voce digito {} estão na maior idade e {} são menores de idade'.format(7 - i, i))
