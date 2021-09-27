while True:
    i = 0
    print(f'-' * 30)
    n = int(input('Querver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    while True:
        if i > 10:
            break
        print(f'{n} x {i} = {n * i}')
        i += 1
print(f'-' * 30)
print('{:^30}'.format('PROGRAMA TABUADA ENCERRADO, Volte sempre'))
print('-' * 30)
