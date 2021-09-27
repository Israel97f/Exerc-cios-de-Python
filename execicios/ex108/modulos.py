from ex107b import moeda


# Programa Principal
n = float(input('Digite um preço: '))
print(f'O dobro do preço é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade do preço é {moeda.moeda(moeda.metade(n))}')
print(f'O preço reduzido é {moeda.moeda(moeda.diminuir(n, 34))}')
print(f'O preço elevado é {moeda.moeda(moeda.aumentar(n, 45))}')
