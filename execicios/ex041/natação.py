from datetime import date

nas = int(input('\033[32mDigite seu ano de nascimento: '))

ida = date.today().year - nas
print('+' * 29)
if ida <= 9:
    print('Sua categoria é MIRIN')
elif ida <= 14:
    print('Sua categoria é INFANTIL')
elif ida <= 19:
    print('Sua categoria é JUNIOR')
elif ida <= 20: 
    print('Sua gategoria é SÊNIOR')
else:
    print('Sua actegoria é MASTER')
print('O atleta tem {} anos'.format(ida))
print('+' * 29)
