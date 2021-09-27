def leiaInt(txt):
    while True:
        try:
            i = int(input(txt))
        except:
            print(f'\033[31mDigite um valor inteiro valido!\033[m')   # ou usar "continue" que retorna ao laço
        else:
            break
        
    return i
    

def leiaFloat(txt):
    while True:
        try:
            f = float(input(txt))

        except (ValueError, TypeError):
            print(f'\033[31mDigite um valor real valido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[32mDigite um valor real valido\033[m')
        else:
            return  f


#PRoograma Principal
n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'Voce digitou {n1} inteiro e {n2} real')
