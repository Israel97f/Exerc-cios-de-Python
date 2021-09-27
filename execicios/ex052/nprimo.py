n = int(input('Digite um numero inteiro: '))
i = 0
for c in range(1, n + 1):
    if n % c == 0:
        i += 1
        print('\033[32m{}'.format(c), end=' ')
    else:
        print('\033[31m{}'.format(c), end= ' ')
if i > 2:
    print(' ')
    print('\033[31m{}\033[m não é primo ele e divisivel por {} números'.format(n, i))
else:
    print(' ')
    print('\33[32m{}\033[m é primo'.format(n))
