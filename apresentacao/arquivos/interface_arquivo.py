def arquivo_existe(nome):
    '''
    Função para verificar se um arquivo existe.
    Parâmetros: nome (str) - nome do arquivo
    Retorna: bool - True se o arquivo existir, False caso contrário
    Função criada por Samuel Vaz
    '''

    try:
        with open(nome, 'r') as arquivo:
            return True
    except FileNotFoundError:
        return False



def criar_arquivo(nome):
    '''
    Função para criar um arquivo.
    Parâmetros: nome (str) - nome do arquivo
    Retorna: None
    Função criada por Samuel Vaz
    '''

    try:
        with open(nome, 'w') as arquivo:
            arquivo.write('tipo; valor; descrição \n')
    except:
        print('Houve um erro ao criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')



def cadastrar_movimento(nome, movimento):
    '''
    Função para cadastrar uma movimentação financeira.
    Parâmetros: nome (str) - nome do arquivo, movimento (dict) - dicionário com os dados da movimentação
    Retorna: None
    Função criada por Samuel Vaz
    '''
    
    try:
        with open(nome, 'a') as arquivo:
            arquivo.write(f'{movimento["tipo"]}; {movimento["valor"]}; {movimento["desc"]} \n')
    except:
        print('Houve um erro!')
    else:
        print('Movimentação financeira cadastrada com sucesso!')