p = float(input('Digite o valor do produto: '))
f = int(input('\033[35mDiga a forma de pagamento; 1 (á vista), 2 (á vita cartão), 3 (2x no cartão), 4 (3x ou mais no cartão)\033[m: '))
flag = 0

print('\033[32m-=' * 30)
if f == 1:
    p = p * 0.9
elif f == 2:
    p = p * 0.95
elif f == 3:
    {

    }
elif f == 4:
    p = p + p * 0.2
else:
    print('\033[33mNão é uma foma valida de pagamento\033[m')
    flag = 1
if flag == 0:
    print('O preso a pagar é {:.2f}'.format(p))
print('-=' * 30)
