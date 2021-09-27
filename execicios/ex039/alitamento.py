from datetime import date
yer = int(input('Digite seu ano de nascimeto: '))
print("""Diga o seu genero biologico
[1] masculino
[2] feminino""")
sexo = int(input('Digite a opição: '))
if sexo == 1:
    ano = date.today().year
    print('\033[33m-=' * 30)
    if ano - yer < 18:
        print('Ainda falta {} anos para você se alista'.format(-1 * ((ano - yer) - 18)))
    elif ano - yer == 18:
        print('Esta na hora de você se alista')
    else:
        print('Ja passou {} anos do tempo para voê se alista'.format(ano - yer - 18))
    print('\/' * 30) #HOOOOH
elif sexo == 2:
    print('-=' * 30)
    print('Você é do sexo feminino logo não precisa cumprir o alistamento obrigatorio')
    print('=-' * 30)
else:
    print('-=' * 30)
    print('Não é uma opção valida')
    print('=-' * 30)