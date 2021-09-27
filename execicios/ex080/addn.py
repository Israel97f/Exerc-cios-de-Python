lista = []
cont = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))    
    if c == 0 or n >= max(lista):
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        while True:
            if n < lista[cont]:
                lista.insert(cont, n)
                print(f'Adicionado na posição {cont} da lista...')
                break
            cont += 1
print('\033[34m-=\033[m' * 30)
print(f'Os valores digitados em ordem foram {lista}')
