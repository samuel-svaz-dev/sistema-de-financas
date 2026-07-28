from rich import print
from rich.panel import Panel

class Transacao:

    def __init__(self, tipo : str, valor : float, descricao : str):
        self.tipo = tipo.upper()
        self.valor = valor
        self.descricao = descricao.upper()

    def exibir(self):
        if self.tipo == 'RECEITA':
            extrato = Panel(f'Valor: R${self.valor:.2f}\nDescrição: {self.descricao}', title = f'RECEITA', width = 40, style = 'green')
            print(extrato)
        elif self.tipo == 'DESPESA':
            extrato = Panel(f'Valor: R${self.valor:.2f}\nDescrição: {self.descricao}', title = f'DESPESA', width = 40, style = 'red')
            print(extrato)
        else:
            print('Foi digitado um valor incorreto!')
