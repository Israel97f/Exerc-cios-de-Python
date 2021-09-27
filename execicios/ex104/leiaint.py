def leiaint(txt):
    while True:
        num = str(input(f'{txt}'))
        if num.isnumeric():
            break
            #return num
        else:
            print(f'\033[31mERRO! digite um numero ineiro\033[m')
    return num


#Programa Principal
n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
