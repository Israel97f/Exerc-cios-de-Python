n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a rasão da PA: '))
soma = n1
i = 0
s = 0
while soma < (n1 + n2 * (10 + s)):
    print('\033[36m{}'.format(soma), end=' > ')
    soma += n2
    if 9 + s == i: 
        t = int(input('\nVoçê quer mostra mais qunatos termos: '))
        s += t
    i += 1
print('\033[34mAcabo!\033[m')
