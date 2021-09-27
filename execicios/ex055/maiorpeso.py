maior = 0
menor = 0
for c in range(0,5):
    n = float(input('Digite um peso em kg: '))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('\033[32mO maior peso foi {} e o menor foi {}'.format(maior, menor))
