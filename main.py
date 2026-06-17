import time
from apresentacao import ui
import funcoes_calculo
from funcoes_calculo.movimentacoes import saldo_atual


# Programa Principal
saldo = 0
movimentos = []

while True:
    ui.mostrar_menu()
    
    escolha = funcoes_calculo.movimentacoes.leiamenu('\nEscolha uma das opções: ')
    time.sleep(1)

    if escolha == 1:
        saldo = funcoes_calculo.movimentacoes.adicionar_receita(saldo, movimentos)

        saldo_atual(saldo)

    elif escolha == 2:
        saldo = funcoes_calculo.movimentacoes.adicionar_despesa(saldo, movimentos)

        saldo_atual(saldo)

    elif escolha == 3:
        funcoes_calculo.movimentacoes.mostrar_saldo(saldo)

    elif escolha == 4:
        funcoes_calculo.movimentacoes.mostrar_extrato(movimentos)

    elif escolha == 0:
        funcoes_calculo.movimentacoes.sair_sistema()
        break

    else:
        print('COMANDO INVÁLIDO! TENTE NOVAMENTE'.center(60))
