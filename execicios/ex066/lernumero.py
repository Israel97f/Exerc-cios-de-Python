s = 0
i = 0
while True:
    n = int(input('Digite un número [999 para sair]: '))
    if n == 999:
        break
    s += n
    i += 1
print(f'\033[33mA soma dos {i} foi {s}')
