def voto(nasc):
    from datetime import date
    ida = date.today().year - nasc
    if ida >= 18 and 65 > ida :
        return f'Com {ida} Voto é obrigatorio'
    elif 18 > ida and 16 <= ida or 65 <= ida :
        return f'Com {ida} Voto é opcional'
    else:
        return f'Com {ida} voto é negado'


#Programa Principal
ida = int(input('Qual o ano em que você nasceu? '))
print(voto(ida))
