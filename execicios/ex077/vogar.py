tupla = ('TRABALHO', 'ESPERA', 'FETICHE', 'MACACO', 'BANANA', 'LEITE', 'VELHO', 'LIXO', 'BOI', 'CHUPETA', 'BARALHO' )
cha = ''
for c in tupla:
    cha = ''
    for e in range(0, len(c)):
        if c.lower()[e] in 'aeiou':
            cha += c.lower()[e] + ' '
    print(f'\033[36mNa palavra {c} temos {cha}\033[m')
