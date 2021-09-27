dicionario = dict()
gols = list()
s = 0
dicionario['jogador'] = str(input('Nomedo jogador: ')).strip()
n = int(input('Quantas partidas ele jogou? '))
for v in range(0, n):
    g = int(input(f'Quantos gols na partida {v}: '))
    gols.append(g)
    s += g
dicionario['gols'] = gols[:]
dicionario['Aproveitamento'] = s
print('-=' * 30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dicionario["jogador"]} jogol {n} partidas.')
for i in range(0, len(dicionario['gols'])):
   print(f'    => Na partida {i} fez {dicionario["gols"][i]} gols')
print(f'O jogador {dicionario["jogador"]} fez {s} gols.')
