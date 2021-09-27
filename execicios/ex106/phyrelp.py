from time import sleep
def pyhelp(txt):
    print('\033[33m')
    help(txt)
    print('\033[m')

def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  \033[32m{txt}\033[m')
    print('~' * (len(txt) + 4))


#Programa Principal
while True:
    escreva('SISTEMA DE AJUDA Pyhelp')
    sleep(0.5)
    comand = str(input('Função ou Biblioteca >> '))
    if comand.strip().upper() == 'FIM':
        sleep(0.5)
        escreva('Até logo')
        break


    escreva(f'Acessando o manual do comando {comand}')
    sleep(0.5)
    pyhelp(comand)
