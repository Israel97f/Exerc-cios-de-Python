n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a rasão da PA: '))
soma = n1
while soma < (n1 + n2 * 10):
    print('\033[36m{}'.format(soma), end=' > ')
    soma += n2
print('\033[34mAcabo!\033[m')
