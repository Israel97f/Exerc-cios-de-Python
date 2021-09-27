n = int(input('Digite um número: '))
p = 1
cont = 0
while cont < n:
    p = p * (n - cont)
    cont += 1
print('\033[33mO fatorial de {} é {}'.format(n, p))
