km = int(input('Qual a distancia da sua viagem em km? '))
preco = 0

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45

print('O preço da sua passagem é {:.2f}'.format(preco))
