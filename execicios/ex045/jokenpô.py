from random import randint
from time import sleep
print("""
[1] Tesoura
[2] Pedra
[3] Papel""")
es = int(input('Escolaha a opção: '))
escolhido = ''
jak = 'Tesoura Pedra Papel'
jak = jak.split()
com = randint(1,3)
gan = ''
gan1 = ''
if com == 1 and es == 2 or com == 2 and es == 3 or com == 3 and es == 1:
    gan = 'Ganhou'
    gan1 = 'Ganha de' 
elif es == com:
    gan = 'Empatamos'
    gan1 = 'Empata com'
else:
    gan = 'Perdeu'
    gan1 = 'perde para'
    
print('\033[36m-=' * 30)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!')
print('{}, {} {} {}'.format(gan, jak[es -1], gan1, jak[com -1]  ))
print('-=' * 30)
