from datetime import date
dicionario = dict()
dicionario['Nome'] = str(input('Nome: ')).strip()
n = int(input('Ano de nascimento: '))
dicionario['Idade'] = date.today().year - n
c = int(input('Carteira de trabalho (0 não tem): '))
if c != 0:
    dicionario['CTPS'] = c
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['Salario'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = 35 - (date.today().year - dicionario['contratação']) + dicionario['Idade']
print('-=' * 30)
for k, v in dicionario.items():
    print(f'{k} tem o valor {v}')
