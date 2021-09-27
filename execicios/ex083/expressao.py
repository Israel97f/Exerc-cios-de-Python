s = str(input('Digite uma expresão valida: ')).strip().lower()
lista =[]
i = u = 0
for c in s:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
print(f'{"":)<30}{"":(>30}')
if len(lista) == 0:
    print('Expresão valida')
else:
    print('Expresão invalida')
