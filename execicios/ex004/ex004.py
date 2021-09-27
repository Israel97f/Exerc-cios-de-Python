n = input('digite algo: ')

print('o tipo primitivo é ',type(n))
print('é um numero ', n.isnumeric() )
print('é alfanumerico',n.isalpha() )
print('é somente espaços',n.isspace() )
print('esta capitalizada', n.istitle())
