n = int(input('Digite o primeiro termo da PA : '))
r = int(input('Digiite a razão da PA: '))

for c in range(n, (r * 10) + n, r):
    print('\033[32m{}'.format(c), end=' ¬ ')
