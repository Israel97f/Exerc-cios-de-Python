s = 0
n1 = 0
while n1 != 999:
    n1 = int(input('Digite um numero: '))
    if n1 != 999:
        s += n1
print('\033[32mA soma de todos os números foi {}'.format(s))
