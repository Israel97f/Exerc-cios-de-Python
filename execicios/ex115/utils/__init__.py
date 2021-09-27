def lin(num=60):
    print('_' * num)


def write(txt):
    lin()
    print(f'{txt:^60}')
    lin()


def readInt(txt):
    while True:
        try:
            num = int(input(txt))
        except:
            print('\033[31mErro! Digite um numero valido\033[m')
        else:
            break
    return num


def menu(lista):
    i = 0
    write('Menu')
    for c in lista:
        i += 1
        print(f'\033[33m{i} - \033[34m{c}\033[m')
    lin()
    opc = readInt('\033[33mSua opção:\033[m ')
    return opc
