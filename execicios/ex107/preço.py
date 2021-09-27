from ex107b import moeda
n = float(input('Digite um preço: '))
print(f'O dobro do preço é R${moeda.dobro(n):.2f}')
print(f'A metade do prço é R${moeda.metade(n):.2f}')
print(f'Almentando o preço fica R${moeda.aumentar(n, 14):.2f}')
print(f'Diminuindo o preço fica R${moeda.diminuir(n, 23):.2f}')
