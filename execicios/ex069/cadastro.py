print('-=' * 30)
print('{:^12}'.format('CADASTRE UM PESSOA'))
print('=-' * 30)
print('--' * 30)
mai = mul = hom = 0
while True:
    n = int(input('Idade: '))
    while True:
        s = str(input('Sexo [M/F]: ')).strip().lower()[0]
        if  s in 'MmFf':
            break
    if n > 18:
        mai += 1
    if s == 'm':
        hom += 1
    if s == 'f' and n < 20:
        mul += 1
    while True:
        p = str(input('Quer casdastrar mai uma pessoa [S/N]: ')).strip().lower()[0]
        if p in 'sn':
            break
    if p == 'n':
        break
print(f"""
Total de pesoas com mais de 18: {mai}
Ao todo {hom} homens cadastrados
E temos {mul} com menos de 20 anos
""")
