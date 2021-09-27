from random import randint
from time import sleep as s
n = int(input('Quuantos jogos quer gerar? '))
n2 = 0
dados = list()
jogo = list()
for c in range(0, n):
    while len(dados) < 6:
        n2 = randint(1, 60)
        if not n2 in dados:
            dados.append(n2)
    jogo.append(dados[:])
    dados.clear() 
print(F'{"-=-=-=-=-="} SORTEANDO {n} JOGOS {"-=-=-=-=-="}')
for d in range(0, len(jogo)):
    print(f'Jogo {d + 1:2}: {jogo[d]}')
    s(0.5)
print(f'{"-=-=-=-=-=-="}{" < BOA SORTE! > "}{"-=-=-=-=-=-="}')
