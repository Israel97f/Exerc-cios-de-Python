from ex107b import moeda


# Programa Principal
n = float(input('Digite um preço: '))
print(f'O dobro do preço é {moeda.dobro(n, True)}')
print(f'A metade do preço é {moeda.metade(n, True)}')
print(f'O preço reduzido é {moeda.diminuir(n, monetario=True)}')
print(f'O preço elevado é {moeda.aumentar(n, 45)}')
