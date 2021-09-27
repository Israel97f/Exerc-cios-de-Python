print('==' * 30)
print('\033[32m{:^60}\33[m'.format('LISTAGEN DE PRODUTOS'))
print('==' * 30)

tupla = ('Pão', 1.00, 'Frango', 4.50, 'Leite', 4.60, 'Picanha', 12.90,'Leite Condesado', 2.45, 'Abacate', 6.20, 'Cenoura', 3.00)
for c in range(0, len(tupla), 2):
    print('{:.<51}R${:>7.2f}'.format(tupla[c],tupla[c+1]))
print('==' * 30)
 