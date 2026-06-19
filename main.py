from time import sleep
import apresentacao.ui
import funcoes_calculo.movimentacoes



# Programa Principal
saldo = 0
movimentos = []

while True:
    apresentacao.ui.mostrar_menu()
    
    escolha = funcoes_calculo.movimentacoes.leiamenu('\nEscolha uma das opções: ')
    sleep(1)

    if escolha == 1:
        saldo = funcoes_calculo.movimentacoes.adicionar_receita(saldo, movimentos)

        funcoes_calculo.movimentacoes.saldo_atual(saldo)

    elif escolha == 2:
        saldo = funcoes_calculo.movimentacoes.adicionar_despesa(saldo, movimentos)

        funcoes_calculo.movimentacoes.saldo_atual(saldo)

    elif escolha == 3:
        funcoes_calculo.movimentacoes.mostrar_saldo(saldo)

    elif escolha == 4:
        funcoes_calculo.movimentacoes.mostrar_extrato(movimentos)

    elif escolha == 0:
        funcoes_calculo.movimentacoes.sair_sistema()
        break

    else:
        print('COMANDO INVÁLIDO! TENTE NOVAMENTE'.center(60))
