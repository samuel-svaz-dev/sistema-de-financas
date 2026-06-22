import apresentacao.formatacao
from time import sleep


def leiamenu(mensagem):
    '''
    Função para ler a opção do menu, garantindo que a entrada seja válida.
    Parâmetros:
    - mensagem: mensagem a ser exibida para o usuário
    Retorna: a opção escolhida pelo usuário
    Função criada por Samuel Vaz
    '''

    while True:
        try:
            n = int(input(mensagem))
            if n in [0, 1, 2, 3, 4]:
                return n
            else:
                print('Opção inválida! Digite um número entre 0 e 4.')
        except ValueError:
            print('Valor inválido! Digite um número inteiro.')

def saldo_atual(saldo):
    '''
    Função para mostrar o saldo atual após uma movimentação, destacando o valor atualizado.'''

    apresentacao.formatacao.texto(f'Saldo ATUAL R${saldo:.2f}', 3)
    apresentacao.formatacao.texto('-'*60, 3)


def leiafloat(mensagem):
    '''
    Função para ler um número float, garantindo que a entrada seja válida.
    Parâmetros:
    - mensagem: mensagem a ser exibida para o usuário
    Retorna: o número float lido
    Função criada por Samuel Vaz
    '''

    while True:
        try:
            n = float(input(mensagem))
            return n
        except ValueError:
            print('Valor inválido! Digite um valor Real.')


def adicionar_receita(saldo, movimentos):
    '''
    Função para adicionar uma receita, atualizando o saldo e o extrato.
    Parâmetros:
    - saldo: valor atual do saldo
    - movimentos: lista de movimentações
    Retorna: o novo saldo atualizado
    Função criada por Samuel Vaz
    '''

    apresentacao.formatacao.texto('Opção 1 - Receita foi escolhida!', 2)

    receita = leiafloat('\033[1;30;42mDigite o valor da Receita R$\033[m')
    descricao = input('\033[1;30;42mDescrição (salário, presente, freelance): \033[m')
    sleep(0.5)

    movimentos.append({
        "tipo": "Receita",
        "valor": receita,
        "desc": descricao
    })

    saldo += receita
    sleep(1)

    return saldo



def adicionar_despesa(saldo, movimentos):
     '''
     Função para adicionar uma despesa, atualizando o saldo e o extrato.
     Parâmetros:
     - saldo: valor atual do saldo
     - movimentos: lista de movimentações
     Retorna: o novo saldo atualizado
     Função criada por Samuel Vaz
     '''


     apresentacao.formatacao.texto('Opção 2 - Despesa foi escolhida!', 1)
     
     despesa = leiafloat('\033[1;30;41mDigite o valor da despesa: R$\033[m')
     sleep(0.5)

     if despesa > saldo:
         print('\033[1;30;41mNão foi possível realizar sua movimentação. Revise seu saldo!\033[m')
         return saldo
          
     descricao = str(input('\033[1;30;41mDescrição (alimentação, lazer, aluguel): \033[m'))
     sleep(0.5)

     movimentos.append({
         "tipo": "Despesa",
         "valor": despesa,
         "desc" : descricao
     })

     saldo -= despesa

     return saldo


def mostrar_saldo(saldo):
    '''
    Função para mostrar o saldo atual.
    Parâmetros:
    - saldo: valor atual do saldo
    Retorna: None
    Função criada por Samuel Vaz
    '''


    sleep(0.5)
    print('-'*60)
    print('Calculando o saldo atual...')
    print('-'*60)
    sleep(0.5)
    apresentacao.formatacao.texto(f'O saldo atual é de R${saldo:.2f}.', 5)
    print('-'*60)


def mostrar_extrato(movimentos):
    '''
    Função para mostrar o extrato atualizado.
    Parâmetros:
    - movimentos: lista de movimentações
    Retorna: None
    Função criada por Samuel Vaz
    '''


    sleep(1)
    print('-'*60)
    print('Buscando todas movimentações da conta...')
    print('-'*60)
    sleep(1)

    apresentacao.formatacao.titulo('EXTRATO ATUALIZADO')

    if len(movimentos) == 0:
        print('Sem movimentações na conta!')
        print('-' * 60)

    else:
        print(f'{"Nº":<5}{"Tipo":<15}{"Valor (R$)":<15}{"Descrição"}')

        for i, c in enumerate(movimentos, start=1):
            print(f'{i:<5}{c["tipo"]:<15}R$ {c["valor"]:>10.2f}   {c["desc"]}')
            sleep(0.5)

        print('-'*60)


def sair_sistema():
    '''
    Função para sair do sistema, exibindo uma mensagem de despedida.
    Parâmetros: None
    Retorna: None
    Função criada por Samuel Vaz
    '''


    apresentacao.formatacao.titulo('Saindo do Sistema...')
    sleep(1)
    apresentacao.formatacao.titulo('OBRIGADO POR UTILIZAR NOSSO PROGRAMA!')
    apresentacao.formatacao.titulo('PORGRAMA ENCERRADO! VOLTE SEMPRE!')
    