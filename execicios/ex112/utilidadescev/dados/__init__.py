def leiadinheiro(txt):
    while True:
        din = str(input(f'{txt}')).replace(',', '.').strip()
        if din.isalpha() or din == '':
            print(f'\033[31mErro! "{din}" é um preço invalido\033[m')
        else:
            break
    return float(din)
