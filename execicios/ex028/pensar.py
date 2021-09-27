from random import randint

number = randint(0, 5)
pesn = int(input('Que numero eu pensei entre 0 e 5? '))
if pesn == number:
    print('Você acertou, parabens')
else:
    print('Você errou, lamento')
    