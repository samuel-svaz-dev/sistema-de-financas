from time import sleep

import funcoes_calculo.movimentacoes

from apresentacao.formatacao import texto, titulo


def mostrar_menu(saldo):
    '''
    mostrar_menu()
    Função para exibir o menu de opções do sistema
    Parâmetros: None
    Retorna: None
    Função criada por Samuel Vaz
    '''
    menu = (
        (1, 'Receita'),
        (2, 'Despesa'),
        (3, 'Saldo'),
        (4, 'Extrato'),
        (0, 'Sair')
    )

    titulo('MENU DE OPÇÕES - SISTEMA DE FINANÇAS PESSOAIS')
    texto(f'{" " * 20}{"Nº":<5}{"OPÇÃO":<20}', 3)
    texto('-'*60, 3)

    for i, o in menu:
        texto(f'{" " * 20}{i:<5}{o:<20}', 3)
        sleep(0.5)
    texto('-'*60, 3)