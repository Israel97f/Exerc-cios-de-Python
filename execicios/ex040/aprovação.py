n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

med = (n1 + n2) / 2
print('-=' * 30)
if med < 5:
    print('\033[31mREPROVADO\033[m')
elif 5 < med < 6.9:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO\033[m')
print('-=' * 30)
