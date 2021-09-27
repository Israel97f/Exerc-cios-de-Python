n = int(input('digite um numero de 1 a 9: '))
print('-=' * 30)
for c in range(0, 10):
    print('\033[34m{} x {} = {:2}\033[m'.format(c, n, c * n))
print('-=' * 30)
