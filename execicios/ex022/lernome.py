nome = str(input('Qual seu nome? '))

print(nome.upper())
print(nome.lower())

dividido = nome.split()
numer = len(nome) - nome.count(' ')
print(numer)
print(len(dividido[0]))
