def arquivoExite(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        #print('\033[31mArquivo não encontrado\033[m')
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('\033[31mOuve um probllema ao criar o arquivo\033[m')
    else:
        print(f'\033[32mSucesso ao criar o arquivo\033[m')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('\033[31mOuve um probllema ao ler o arquivo\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]} anos')
    finally:
        a.close()


def escreverArquivo(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mOuve um probllema ao abri arquivo\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mOuve um probllema ao escrever dados no arquivo\033[m')
        else:
            print('\033[32mPessoa cadastrada com sucesso\033[m')
    finally:
        a.close()
