velo = int(input('Qual a velocidade do carro? '))

if velo > 80:
    multa = (velo - 80) * 7
    print('Você ultrapassou o limite de velocidade sua multa é de {:.2f}'.format(multa))
