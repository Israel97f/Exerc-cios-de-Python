lista = [[], []]
n = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-=' * 30)
print(f'Os valores pares digitado foram: {sorted(lista[0])}')
print(f'Os valores impares digitado foram: {sorted(lista[1])}')
