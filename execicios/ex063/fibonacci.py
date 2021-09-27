n1 = int(input('Digite quantos termos deseja: '))
i = 0
t = 0
i2 = 0
a1 = 0
a2 = 0
while i < n1:
    i2 += 1
    if i == 0:
        print('0 > 1 > 1',end=' > ')
        t = 1
    if i2 == 1:
        a2 = t
    if i2 == 2:
        a1 = t
        i2 = 0
    
    t = a1 + a2
    #a1 = a2
    #a2 = t
    if i > 0:
        print(t, end=' > ')
    i += 1
