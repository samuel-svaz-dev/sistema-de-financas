def arquivo_existe(nome):
    try:
        with open(nome, 'r') as arquivo:
            return True
    except FileNotFoundError:
        return False



def criar_arquivo(nome):
    try:
        with open(nome, 'w') as arquivo:
            arquivo.write('tipo; valor; descrição \n')
    except:
        print('Houve um erro ao criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')



def cadastrar_movimento(nome, movimento):
    try:
        with open(nome, 'a') as arquivo:
            arquivo.write(f'{movimento["tipo"]}; {movimento["valor"]}; {movimento["desc"]} \n')
    except:
        print('Houve um erro!')
    else:
        print('Movimentação financeira cadastrada com sucesso!')