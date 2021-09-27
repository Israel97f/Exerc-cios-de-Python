from time import sleep
def maior(* num):
    k = 0
    cont = 0
    for v in num:
        if k == 0:
            m = v
        if v > m:
            m = v
        k = + 1
    print('--' * 20)
    print('Analizando os dados...')
    if len(num) > 0:
        while cont < len(num):
            print(f'{num[cont]}', end=' ', flush=True)
            sleep(0.5)
            cont += 1

        print(f'foram informados {len(num)} valores ao todo ')
        print(f'O maior valor informado foi {m}')
    else:
        print(f'foram informados {0} valores ao todo ')
        print(f'O maior valor informado não existe')
    print('--' * 20)


# Programa Principal
maior(3, 4, 4, 5, 8, 7, 9, 0)
maior(2, 3, 4)
maior(7)
maior()