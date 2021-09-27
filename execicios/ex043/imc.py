pe = float(input('Digite seu peso: '))
al = float(input('Digite sua autura: '))

imc = pe / al ** 2
est = ''

if imc < 18.5:
    est = 'Abaixo do peso'
elif 18.5 <= imc <= 25:
    est = 'Peso ideal'
elif 25 < imc <=30:
    est = 'Sobrepeso'
else:
    est = 'Obesidade morbida'

print('\033[31m-=\033[m' * 30)
print(imc, est)
print('\033[32m-=\033[m' * 30)
