dicionario = dict()
jogadores = list()
gols = list()
s = 0
i = 0
while True:
    dicionario['jogador'] = str(input('Nomedo jogador: ')).strip()
    n = int(input('Quantas partidas ele jogou? '))
    for v in range(0, n):
        g = int(input(f'Quantos gols na partida {v}: '))
        gols.append(g)
        s += g
    dicionario['gols'] = gols[:]
    dicionario['Aproveitamento'] = s
    jogadores.append(dicionario.copy())
    dicionario.clear()
    gols.clear()
    s = 0
    print('-=' * 30)
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        else:
            print('opção invalida porfavor tente novamente')
    if r in 'N':
        break
print('==' * 30 )
print(f'{"cod":^5}{"nome":<15}{"gols":<15}{"total":>25}')
print('==' * 30)
for v in jogadores:
    p = (35 - (len(v['gols']) * 3))
    print(f'{i:^5}{v["jogador"]:<15}{v["gols"]}{" " * p}{v["Aproveitamento"]:<5}')
    print('--' * 30)
    i += 1
while True:
    u = int(input('Mostrar dados de qual jogador? '))
    if len(jogadores) > u and u >= 0:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[u]["jogador"]}: ')
        for v in range(0, len(jogadores[u]['gols'])):
            print(f'No jogo {v} fez {jogadores[u]["gols"][v]} gols ')
        print('--' * 30)
    elif u == 999:
        break
    else:
        print(f'Numero invalido, tente novamente.')
print('<< Voute sempre >>')
