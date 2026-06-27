def arquivo_existe(nome):
    '''Verifica se o arquivo existe. Retorna True se existir e False se não existir.'''

    try:
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    
    else:
        return True
    


def cadastrar_movimento(arq, movimento):
    '''
    Função para cadastrar um novo movimento no arquivo.
    Parâmetros: arq (string) - nome do arquivo, movimento (dict) - dicionário com os dados do movimento
    Retorna: None
    Função criada por Samuel Vaz
    '''

    
    try:
        a = open(arq, 'a')
    except:
        print('Erro ao ler o arquivo!')
    else:
        try:
            a.write(f'{movimento["tipo"]};{movimento["valor"]};{movimento["desc"]}\n')
        except:
            print('Erro ao escrever dados')
        else:
            print(f'Novo registro de {movimento["tipo"]} adicionado.')
        finally:
            a.close()


#a = open(arq, 'a')
#a.write(f'{movimento["tipo"]};{movimento["valor"]};{movimento["desc"]}\n')