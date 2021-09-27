cadastro = list()
aluno = list()
notas = list()

while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota: ')))
    notas.append(float(input('Nota: ')))
    aluno.append(notas[:])
    cadastro.append(aluno[:])
    aluno.clear()
    notas.clear()
    while True:
        r = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
        if r in 'sn':
            break
    if r in 'n':
        break
print('-=' * 30)
print(f'{"No.":<5}{"NOME":<20}{"MÉDIA":>35}')
print('--' * 30)
for c, v in enumerate(cadastro):
    print(f'{c:<5}{v[0]:<20}{(v[1][0] + v[1][1])/2:35.1f}')
print('--' * 30)
while True:
    while True:
        alu = int(input('Mostar notasde qual aluno? (999 interrompe): '))
        if alu < len(cadastro) or alu == 999:
            break
        else:
            print('Indixe invalido!, Tente novamente')
    if alu == 999:
        break
    print(f'Notas de {cadastro[alu][0]} são {cadastro[alu][1]}')
