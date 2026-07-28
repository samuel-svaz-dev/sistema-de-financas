from rich import print
from rich.panel import Panel
from src.modelos.conta import Conta
from src.modelos.transacao import Transacao


minha_conta = Conta(101, 'Samuel')

while True:
    menu_de_opcoes = f'[green]1 - RECEITA[/]\n[red]2 - DESPESA[/]\n[magenta]3 - EXTRATO[/]\n[white]0 - SAIR[/]'
    menu = Panel(f'{menu_de_opcoes}', title = 'MENU DE OPÇÕES', width = 30, style = 'blue')
    print(menu)
    opcao = input('Digite a opção escolhida ou 0 para sair!')
    if opcao == '1':
        valor_receita = float(input('[green]Digite o valor da Receita R$[/]'))
        desc_receita = str(input('[green]Digite a descrição da Receita: [/]'))
        nova_receita = Transacao('RECEITA', valor_receita, desc_receita)
        minha_conta.adiciona_transacao(nova_receita)
    elif opcao == '2':
        valor_despesa = float(input('[red]Digite o valor da Despesa R$[/]'))
        desc_despesa = str(input('[red]Digite a descrição da Despesa[/]'))
        nova_despesa = Transacao('DESPESA', valor_despesa, desc_despesa)
        minha_conta.adiciona_transacao(nova_despesa)
    elif opcao == '3':
        minha_conta.exibir_extrato()
    elif opcao == '0':
        break
    else:
        print('[bold white red]OPÇÃO INVÁLIDA![/]')
