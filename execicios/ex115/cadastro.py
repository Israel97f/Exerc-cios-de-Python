import utils
from time import sleep
import arquivo

arq = 'lista de cadastro'
if not arquivo.arquivoExite(arq):
    arquivo.criarArquivo(arq)
while True:
    res = utils.menu(['Pessoas cadastradas',
                'Cadastra nova pessoa',
                'Sair do sistema'])

    sleep(0.5)
    if res == 1:
        utils.write('Pessoas cadastradas')
        arquivo.lerArquivo(arq)
    elif res == 2:
        utils.write('Cadastrar Pessoa')
        nome = str(input('Nome: '))
        idade = utils.readInt('Idade: ')
        arquivo.escreverArquivo(arq, nome, idade)
    elif res == 3:
        utils.write('Saindo do sitema...Obrigado!')
        break
    else:
        print('\033[31mErro! Digite uma opção valida\033[m')
    sleep(2)
