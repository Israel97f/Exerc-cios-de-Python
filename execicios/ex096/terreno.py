def área( l, c):
    ar = l * c
    print(f'A área do seu terreno é {ar} m²')


#Programa Principal
print('--' * 30)
print(f'{"Controle de terreno":^60}')

a = float(input('Comprimento do terreno [m]? '))
b = float(input('Largura do terreno [m]? '))
área(a, b)
