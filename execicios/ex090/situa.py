dicionario = dict()
dicionario['nome'] = str(input('digite um nome do  aluno: ')).strip()
dicionario['media'] = float(input(f'digie a média de {dicionario["nome"]}:' ))
if dicionario['media'] >= 6:
    dicionario['situação'] = 'Aprovado'
else:
    dicionario['situação'] = 'Reprovado'
for k, v in dicionario.items():
    print(f'{k} é igual a {v}')
