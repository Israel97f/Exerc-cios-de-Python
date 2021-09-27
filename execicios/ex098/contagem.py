from time import sleep
def contagem (inicio, fim, passo):
    if passo == 0:
        passo = 1
        
    if fim - inicio >= 0:
        k = 1
    else:
        k = -1
        if passo > 0:
            passo = - passo

    print('--' * 20)
    print(f'Comtagem de {inicio} áte {fim} de {passo} em {passo}')
    for i in range(inicio, fim + k , passo):
        print(f'{i}', end=' ', flush=True)
        sleep(0.1)
    print('FIM!')
    print('--' * 20)


#Programa principal
contagem(1, 10, 1)
contagem(10, 1, -2)
contagem(30, 1, -8)
print('Agora é sua vez de fazer a comtagem')
p1 = int(input('Inicio: '))
p2 = int(input('fim: '))
p3 = int(input('passo: '))
contagem(p1, p2, p3)
