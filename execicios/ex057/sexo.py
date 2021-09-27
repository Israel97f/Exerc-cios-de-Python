s = ' '
while not s  in  'mf':
    s =str(input('\033[32mSexo [M/F]: ').strip().lower())
    if not s in 'mf':
        print('\033[31m Opção invalida tente novamente! ')
