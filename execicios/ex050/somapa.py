s = 0
for c in range(0, 6):
    n = int(input('digite um numero: '))
    if n % 2 == 0:
        s += n
print('\033[36mA soma é {}'.format(s))
