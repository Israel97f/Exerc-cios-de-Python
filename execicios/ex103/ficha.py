def ficha(nome='<Desconhecido>', gols=0):

    return f'O jogador {nome} fez {gols} gols no campeonato'


#Programa Principal
nom = str(input('Qual o nome do jogador? '))
go = str(input('Quantos gols o jogador fez? '))
if go.isnumeric():
    go = int(go)
else:
    go = 0
if nom.strip() == '':
    print(ficha(gols=go))
else:
    print(ficha(nom, go))
