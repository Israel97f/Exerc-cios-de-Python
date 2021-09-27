from random import randint

com = randint(0, 10)
n = -1
cont = 0
while not com == n:
    n = int(input('Em que numero acha que estou punsando?: '))
    cont += 1
print('\033[33mAcertou eu estava pensando no número {} e leuvo {} tentativas para isso'.format(com, cont))
