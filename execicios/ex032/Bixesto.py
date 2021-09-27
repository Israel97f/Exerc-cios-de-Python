from datetime import date

ano = int(input('Diga um ano (Coloque zero ara analizar o ano atual): '))

res = ano - 2016
if ano == 0:
    ano = date.today().year
print('=' * 20)
if (ano - 2016) % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('({}) é bissexto'.format(ano))
else:
    print('({}) não é bissexto'.format(ano))
print('=' * 20)
