import random

a1 = str(input(' diga o nome do aluno 1 ')) 
a2 = str(input(' diga o nome do aluno 2 '))
a3 = str(input(' diga o nome do aluno 3 '))
a4 = str(input(' diga o nome do aluno 4 '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('O aluno soteado é o aluno {}'.format(lista))