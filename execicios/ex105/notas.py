def notas(*lista, sit=False):
    """-->Função para analizar notas é situação de varios lunos
    :param n: notas dos alunos
    :param sit: valor opcional indicando se deve ou não adicionar a situação 
    :return: retorna um dicionario con varias informações sobre a situação do turma
    """
    cont = 0
    maior = 0
    menor = 0
    diario = dict()
    media = sum(lista)/len(lista)
    for c in lista:
        if cont == 0:
            maior = c
            menor = c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        cont += 1
    diario = {'total':len(lista), 'maior':maior, 'menor':menor, 'media': media}
    if sit == True:
        if media >= 7.0:
            diario['Situação'] = 'Boa'
        elif 7.0 > media > 4.0:
            diario['Situação'] = 'Razoavel'
        else:
            diario['Situação'] = 'Ruin'
    return diario


#Programa Principal
no = notas(4.5, 3.5, 6.8, 8.0, 7.5, 2.5, 7.8, 2.9, 10.0, 9.5, 8.9, 9.8 , 10.0, 10.0, 10.0, sit=True)
print(no)
help(notas)