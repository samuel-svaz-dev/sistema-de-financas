import time
from apresentacao import ui
from funcoes_calculo import movimentacoes

menu = (
    (1, 'Receita'),
    (2, 'Despesa'),
    (3, 'Saldo'),
    (4, 'Extrato'),
    (0, 'Sair')
)


# Programa Principal
saldo = 0
movimentos = []

while True:
    ui.titulo('SISTEMA FINANCEIRO')
    ui.texto(f'{" " * 20} {"Nº":<5}{"OPÇÃO":<20}', 3)
    ui.texto('-'*60, 3)

    for i, o in menu:
        ui.texto(f'{" " * 20} {i:<5}{o:<20}', 3)
    ui.texto('-'*60, 3)
    
    escolha = int(input('\nEscolha uma das opções: '))
    time.sleep(1)

    if escolha == 1:
        saldo = movimentacoes.adicionar_receita(saldo, movimentos)

        ui.texto(f'Saldo ATUAL R${saldo:.2f}', 2)
        print('-' * 60)

    elif escolha == 2:
        saldo = movimentacoes.adicionar_despesa(saldo, movimentos)

        ui.texto(f'SALDO ATUAL R${saldo:.2f}', 1)
        print('-' * 60)

    elif escolha == 3:
        movimentacoes.mostrar_saldo(saldo)

    elif escolha == 4:
        movimentacoes.mostrar_extrato(movimentos)

    elif escolha == 0:
        movimentacoes.sair_sistema()
        break

    else:
        print('COMANDO INVÁLIDO! TENTE NOVAMENTE'.center(60))
