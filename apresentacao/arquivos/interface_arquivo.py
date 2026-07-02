def arquivo_existe(nome):
    '''
    Função para verificar se um arquivo existe.
    Parâmetros: nome (str) - nome do arquivo
    Retorna: bool - True se o arquivo existir, False caso contrário
    Função criada por Samuel Vaz
    '''

    try:
        with open(nome, 'r', encoding='utf-8') as arquivo:
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
        with open(nome, 'w', encoding='utf-8') as arquivo:
            cabecalho = f'{"Tipo":<12} | {"Valor (R$)":<12} | {"Descrição"}\n'
            linha = '-' * len(cabecalho) + '\n'
            arquivo.write(cabecalho)
            arquivo.write(linha)
    except Exception as e:
        print(f'Houve um erro ao criar o arquivo: {e}')
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
        with open(nome, 'a', encoding='utf-8') as arquivo:
            valor_formatado = f'R${movimento["valor"]:.2f}'
            linha = f'{movimento["tipo"]:<12} | {valor_formatado:<12} | {movimento["desc"]}\n'
            arquivo.write(linha)
    except Exception as e:
        print(f'Houve um erro ao cadastrar a movimentação: {e}')
    else:
        print('Movimentação financeira cadastrada com sucesso!')


def exibir_saldo(nome):
    '''
    Função para exibir o saldo atual a partir do arquivo de movimentações.
    Parâmetros: nome (str) - nome do arquivo
    Retorna: float - saldo atual
    Função criada por Samuel Vaz
    '''
    
    try:
        with open(nome, 'r', encoding='utf-8') as arquivo:
            saldo_atual = 0
            for linha in arquivo:
                if 'Receita' not in linha and 'Despesa' not in linha:
                    continue
                pedacos = linha.strip().split('|')
                tipo = pedacos[0].strip()
                valor = float(pedacos[1].strip().replace('R$', ''))
                descricao = pedacos[2].strip()
                if tipo == 'Receita':
                    saldo_atual += valor
                elif tipo == 'Despesa':
                    saldo_atual -= valor
            return saldo_atual
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception as e:
        print(f'Erro ao ler o arquivo {e}')